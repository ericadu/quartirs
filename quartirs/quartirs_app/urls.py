from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.generate_qr, name='index'),
  url(r'^checkins$', views.get_validated_users, name='checkins'),
  url(r'^getCheckedInUsers$', views.get_validated_users_table, name='checkInTable'),
  url(r'^testQR/([0-9a-zA-Z]+)$', views.test_qr, name='testQR'),
  url(r'^([0-9a-zA-Z ]+)$', views.check_in, name='check_in'),
]