from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(label="Password",widget=forms.PasswordInput)
	password2 = forms.CharField(label="ConfirmPassword",widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username","email")

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError("两次输入的密码不匹配")
		return cd['password2']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ("birth","phone")
