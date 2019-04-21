from django.urls import path
from . import views

urlpatterns = [
	path('articles/',views.blog_list,name='blog_list'),
	path(r'articles/<int:article_id>/',views.blog_detail,name='blog_detail'),
]