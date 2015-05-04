from django.shortcuts import render
from django.http import HttpResponse
from mit import scripts_login_decorator
from django.utils.decorators import method_decorator 
import django_socketio

from django.template import RequestContext, loader

# Create your views here.
@scripts_login_decorator
def index(request):
	print request.session
	return render(request, 'quartirs_app/index.html', {})

def check_in(request):
  context = {}
  return render(request, 'quartirs_app/check_in.html', context)

def authenticate_service(request):
	pass

def generate_qr(request):
	pass
def authenticate_requestor(request):
	pass
def get_validated_users(request):
	pass
def ping_client(request):
	django_socketio.broadcast('hello!!');