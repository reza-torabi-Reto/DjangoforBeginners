from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomeUserChangeForm, CustomeUserCreationForm, UserCreationForm, UserChangeForm
from .models import CustomeUser
# Register your models here.

class CustomeUserAdmin(UserAdmin):
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    model = CustomeUser
    list_display = ['username', 'email', 'is_staff','first_name', 'last_name',  'age', 'about']
    fieldsets = UserAdmin.fieldsets + (
        ('Test Nmae', {'fields' : ('age', 'about',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields' : ('age', 'is_superuser','first_name', 'last_name', 'about')}),
    )

admin.site.register(CustomeUser, CustomeUserAdmin)
