from datetime import datetime

from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse

from rango.models import Category
from rango.models import Page, Commit
from rango.forms import CategoryForm
from rango.forms import PageForm
from rango.forms import UserForm, UserProfileForm, CommentForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('rango:index'))


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")  # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rango/login.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rango/register.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'rango/index.html', context=context_dict)
    return response


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


def about(request):
    print("TEST COOKIE WORKED!")
    print(request.method)
    print(request.user)

    context_dict = {}
    context_dict['visits'] = request.session['visits']
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)


def show_page(request, category_name_slug, page_id):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    user_id = request.user
    context_dict = {}
    try:
        pages = Page.objects.get(id=page_id)
        print(page_id)
        category = Category.objects.get(id=pages.category_id)
        users = User.objects.get(username=user_id)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    if request.method == "POST":
        if 'add' in request.POST:

            form = CommentForm(request.POST)
            if form.is_valid():
                comm = form.save(commit=False)
                comm.user = users
                comm.page = pages
                comm.save()
                return redirect(
                    reverse('rango:show_page', kwargs={'category_name_slug': category_name_slug, 'page_id': page_id}))
        if 'like' in request.POST:
            pages.likes = pages.likes + 1
            print(pages.likes)
            pages.save()
    else:
        form = CommentForm()
    context_dict['form'] = form
    context_dict['ties'] = Commit.objects.filter(page_id=page_id)
    return render(request, 'rango/page.html', context=context_dict)


@login_required
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=True)
            print(cat, cat.slug)
            return redirect('rango:index')
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('rango:index')

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))

    else:
        print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)


def add_like(request,category_name_slug,page_id):
    pages = Page.objects.get(id=page_id)
    pages.likes = pages.likes + 1
    pages.save()
    print('这里是参数   sssssssss',category_name_slug,page_id)


    return redirect(reverse('rango:index'))

