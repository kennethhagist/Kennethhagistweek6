from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users$', views.users),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<user_id>\d+)/show$', views.show),
    url(r'^(?P<user_id>\d+)/edit$', views.edit),
    url(r'^(?P<user_id>\d+)/delete$', views.delete)
]
