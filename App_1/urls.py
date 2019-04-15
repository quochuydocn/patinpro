
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home1, name='home1'), # new
    path('control', views.Control, name='control'), # new
    url(r'^detail/(?P<shoe_pk>[0-9]+)/$', views.Detail, name='detail'),
    path('', views.home, name='home'),
]
