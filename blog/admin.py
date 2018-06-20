from django.contrib import admin
from blog.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Title', 'content', 'pub_time')     # 后台控制页面显示的内容
    list_filter = ('pub_time',) # 控制台页面显示的过滤器

admin.site.register(Article, ArticleAdmin)
