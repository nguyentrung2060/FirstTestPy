from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    user_name = forms.CharField(label="Account", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Password is incorrected")

    def clean_userName(self):
        user_name = self.cleaned_data['user_name']
        if not re.search(r'^\w+&', user_name):
            raise forms.ValidationError("UserName not contains special char")
        try:
            User.objects.get(user_name=user_name)
        except User.DoesNotExist():
            return user_name
        raise forms.ValidationError("User was exist")
    
    def clean_save(self):
        User.objects.create_user(username=self.cleaned_data['user_name'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])