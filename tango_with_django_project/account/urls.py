from django.urls import path
from django.contrib.auth import views as auth_views
from account import views
from account import forms

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(
        template_name="account/login.html", authentication_form=forms.MyAuthenticationForm),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name="account/change_password.html",), name='change_password'),
    path('change_username/', views.ChangeUserNameView.as_view(), name='change_username'),
    path('change/avatar/', views.ChangeAvatarView.as_view(), name='change_avatar'),

]