
from django import forms
from home.models import MyUser


class SignupModelForm(forms.ModelForm):
    class Meta:
        model = MyUser

        fields = [
            'username',
            'email',
            'phone_number',
            'password'
        ]
