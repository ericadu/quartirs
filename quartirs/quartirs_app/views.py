from django.shortcuts import render
from django.http import HttpResponse
from mit import scripts_login_decorator
from django.utils.decorators import method_decorator 

from django.template import RequestContext, loader

# Create your views here.
@scripts_login_decorator
def index(request):
	return render(request, 'quartirs_app/index.html', {})

def check_in(request):
  context = {}
  return render(request, 'quartirs_app/check_in.html', context)