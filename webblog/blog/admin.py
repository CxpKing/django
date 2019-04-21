from django.contrib import admin
from .models import BlogArticles
# Register your models here.

#方式1：将表关联到admin后台关联中，但是并不能显示所有字段
#admin.site.register(BlogArticles)

#方式2：新建一个类，用于存放表的字段，并将其与表关联起来，放到admin中时显示的就是盖类的属性了。
class BlogArticlesAdmin(admin.ModelAdmin):
	list_display = ("title","author","publish")
	list_filter = ("publish","author")
	search_fields = ("title","body")
	raw_id_fields = ("author",)
	date_hierarchy = "publish"
	ordering = ["publish","author"]

admin.site.register(BlogArticles,BlogArticlesAdmin)
