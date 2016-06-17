"""
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list),
)
"""
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.post_list),
]
