from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomeUser

class CustomeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomeUser
        # fields = UserCreationForm.Meta.fields + ('age', 'is_staff', 'is_superuser')
        fields = ('username', 'email', 'age', 'is_superuser')


class CustomeUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomeUser
        fields = UserCreationForm.Meta.fields