from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^destroy$', views.destroy),
    url(r'^update$', views.update),
    url(r'^(?P<blog_id>\d+)/show$', views.show),
    url(r'^(?P<blog_id>\d+)/edit$', views.edit),
    url(r'^(?P<blog_id>\d+)/delete$', views.delete)
]
