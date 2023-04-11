from django.contrib import admin
from .models import (
    User,
    UserVerification
)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('verified','otp')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'phone_number', 'name', 'verified', 'is_active', 'is_superuser', "otp")


class CustomUserInline(admin.StackedInline):
    model = User
    can_delete = False
    verbose_name_plural = 'user'


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm   
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'verified', 'is_superuser','otp')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', "phone_number",'password', 'name',"smart_card")}),
        ('Personal', {'fields': ('profile_picture','dob', 'age', "gender")}),
        ('Location', {'fields': ('country', 'address')}),
        ('Verified', {'fields': ('verified','otp',)}),
        ('Roles', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone_number', 'email', 'name', 'password1', 'password2', 'groups', 'is_superuser',
                'verified','otp'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# admin.site.unregister(UserAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserVerification)
