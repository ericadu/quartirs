from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext, loader

# Create your views here.
def index(request):
	return render(request, 'quartirs_app/index.html', {})

def check_in(request):
  context = {}
  return render(request, 'quartirs_app/check_in.html', context)