from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
  url(r'^[0-9a-zA-Z ]+$', views.check_in, name='check_in'),
]