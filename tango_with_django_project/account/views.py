import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from notifications.base.models import NotificationQuerySet
from notifications.signals import notify

from account.forms import RegisterForm, UserProfileForm, PageForm, SiteMessageForm
from rango import models as rango_models


# Create your views here.
from rango.models import UserProfile


@login_required
def index(request):
    return render(request, 'account/index.html')


class ChangeUserNameView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'account/change_username.html')

    def post(self, request):
        username = request.POST.get("username", None)
        if not username:
            return HttpResponse("Change Fail")

        request.user.username = username
        request.user.save()
        print(request.user)
        return HttpResponse("Change Success")


class ChangeAvatarView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'account/change_avatar.html')

    def post(self, request):
        file_obj = request.FILES.get("avatar", None)
        if not file_obj:
            return HttpResponse("Change Fail")

        from account.utils.reset_filename import custom_file_name
        file_obj.name = custom_file_name(file_obj)

        user_profile_obj, created = rango_models.UserProfile.objects.get_or_create(user=request.user)
        user_profile_obj.avatar = file_obj
        user_profile_obj.save()

        print(request.user)
        return HttpResponse("Change Success")


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form, })

    def post(self, request):
        '''
        todo:user website
        :param request:
        :return:
        '''
        registered = False
        user_form = RegisterForm(request.POST)
        profile_form = UserProfileForm()
        if user_form.is_valid():
            user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user_form.instance
            profile.website = ""
            profile.save()

            registered = True

        return render(request, 'account/register.html', {'form': user_form, 'registered': registered})


class ManagePages(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'account/manage_pages.html')


class AddPage(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()

        return render(request, 'account/add_page.html', {"form": form})

    def post(self, request):
        result = False
        is_add = True
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page_form = form.save(commit=False)
            page_form.user = request.user
            page_form.save()
            result = True

        return render(request, 'account/add_page.html', {"form": form, "result": result})


class ChangePage(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id", None)
        page_obj = rango_models.Page.objects.get(id=id)
        form = PageForm(instance=page_obj)
        return render(request, 'account/change_page.html', {"form": form})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id", None)
        page_obj = rango_models.Page.objects.get(id=id)
        result = False

        form = PageForm(request.POST, instance=page_obj)
        if form.is_valid():
            form.save()
            result = True

        return render(request, 'account/change_page.html', {"form": form, "result": result})


class DeletePage(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        id = request.GET.get("id", None)
        res = dict(result="Hide success")

        try:
            page_obj = rango_models.Page.objects.get(id=id)
            page_obj.is_show = 0
            page_obj.save()
        except rango_models.Page.DoesNotExist:
            res["result"] = "The requested data does not exist"

        return HttpResponse(json.dumps(res), content_type='application/json')



class NotificationQuerySetNew(NotificationQuerySet):
    def sent_all(self, sender_instance):
        return self.exclude(recipient=sender_instance)


class SiteMessage(LoginRequiredMixin, View):
    def get(self,request):
        site_msg = request.user.notifications

        return render(request, "account/site_message.html",{"site_msg":site_msg,})


class SendMessage(LoginRequiredMixin, View):
    def get(self, request):
        receiver = request.GET.get("receiver",None)
        form = SiteMessageForm(initial={'receiver': receiver})

        return render(request,"account/send_message.html",{"form":form})

    def post(self, request):
        is_send = False
        form = SiteMessageForm(request.POST)
        if form.is_valid():
            try:
                recevicer = User.objects.get(email=form.cleaned_data["receiver"])
                print(recevicer,":recevicer")
                notify.send(request.user, recipient=recevicer, verb=form.cleaned_data["content"])
                is_send = True
            except User.DoesNotExist:
                pass

        return render(request, "account/send_message.html", {"form": form,"is_send":is_send})


class ReadMessage(LoginRequiredMixin, View):
    def get(self, request):
        res = dict(result=False)
        # get unread msg
        notice_id = request.GET.get('notice_id')
        # update one msg
        if notice_id:
            # article = ArticlePost.objects.get(id=request.GET.get('article_id'))
            request.user.notifications.get(id=notice_id).mark_as_read()
            res["result"] = True
            return HttpResponse(json.dumps(res), content_type='application/json')
        # update all msg
        else:
            request.user.notifications.mark_all_as_read()
            res["result"] = True
            return HttpResponse(json.dumps(res), content_type='application/json')