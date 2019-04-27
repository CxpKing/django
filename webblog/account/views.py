from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm
# Create your views here.


def user_login(request):
	'''
	login function
	login_form.is_valid 在创建实例时，如果传递给表单的数据是符合表单类属性要求的，则返回True，否则返回False
	login_form.cleaned_data 以字典的形式返回实例的具体数据。如果传入的某项数据不合法，则在cleaned_data的结果中不予显示。

	'''
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user:
				login(request,user)
				return HttpResponse("Welcome You.You have been authenticated successfully")
			else:
				return HttpResponse("Sorry.Your username or password is not right.")
		else:
			return HttpResponse("Invalid login")
	if request.method == "GET":
		login_form = LoginForm()
	return render(request,"account/login.html",{"form":login_form})

def user_register(request):
	if request.method == "POST":
		user_form = RegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return HttpResponse("注册成功")
		else:
			return HttpResponse("抱歉，你注册失败")
	else:
		user_form = RegistrationForm()
		return render(request,"account/register.html",{"form":user_form})
