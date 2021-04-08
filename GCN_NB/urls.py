from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.login),
    # url(r'^content/$', views.content),
    url(r'^$', views.index),
    # url(r'^fenci/$', views.fenci),
]