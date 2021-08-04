from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

# from rango.models import UserProfile
from rango import models as rango_model


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = u'username'
        self.fields['password'].widget.attrs['placeholder'] = u'password'


class UniqueUserEmailField(forms.EmailField):
    """
    An EmailField which only is valid if no User has that email.
    """

    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Exiting Email")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Exiting Email")
        except User.DoesNotExist:
            pass


class RegisterForm(UserCreationForm):
    email = UniqueUserEmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = rango_model.UserProfile
        fields = ('website', 'picture',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=rango_model.Page.TITLE_MAX_LENGTH,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=rango_model.Page.URL_MAX_LENGTH, help_text="Please enter the URL of the page.")

    class Meta:
        model = rango_model.Page
        exclude = ("views", "likes", "time", "user")


class HaveUserEmailField(forms.EmailField):
    """
    An EmailField which only is valid if no User has that email.
    """

    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise forms.ValidationError("Does Not Exist Email")


class SiteMessageForm(forms.Form):
    receiver = HaveUserEmailField(required=True, help_text="please input email address")
    content = forms.CharField(widget=forms.Textarea,required=True)

