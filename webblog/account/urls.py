from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'account' #命名空间 一定要写这一行，否则html中会报错'account' is not a registered namespace
urlpatterns = [
	#path(r'login/',views.user_login,name = 'user_login'),
	path(r'login/',auth_views.LoginView.as_view(template_name="account/login.html"),name='user_login'),
]
