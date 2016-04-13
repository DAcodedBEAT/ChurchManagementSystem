from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from Accounts.models import UserProfile


class UserRegisterForm(UserCreationForm):
    """
    Creates form to register a user.
    """

    #class Meta:
    #    model = User
    #    fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
"""
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        """


class UserProfileCreateForm(ModelForm):
    """
    Creates form to create UserProfile
    """
    """
    class Meta:
        model = UserProfile
        fields = ('gender', 'DOB', 'DOD', 'bio', 'phone_number')"""


class UserEditForm(UserChangeForm):
    #class Meta:
    #    model = User
    #    fields = ''
    pass


#class UserProfileEditForm(ModelForm):
    """
    Creates form to create UserProfile
    """
"""    class Meta:
        model = UserProfile
        fields = ('location', 'bio', 'phone_number')"""