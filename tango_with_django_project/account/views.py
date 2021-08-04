import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View

from account.forms import RegisterForm, UserProfileForm, PageForm
from rango import models as rango_models


# Create your views here.
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

        request.user.avatar = file_obj
        request.user.save()
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
