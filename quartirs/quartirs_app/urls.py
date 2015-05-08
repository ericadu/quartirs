from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.generate_qr, name='index'),
  url(r'^checkins$', views.get_validated_users, name='checkins'),
  url(r'^([0-9a-zA-Z ]+)$', views.check_in, name='check_in'),
]