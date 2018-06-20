from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^index/$', views.index),
    re_path(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    re_path(r'^new/(?P<article_id>[0-9]+)$', views.new_page, name='new_page'),
    re_path(r'^new/action/$', views.new_action, name='new_action')
]
