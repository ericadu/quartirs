from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.template import RequestContext, loader

from quartirs_app.models import QRTable, ValidatedUsers

# Create your views here.
@login_required
def index(request):
	print request.session
	return render(request, 'quartirs_app/index.html', {})

def check_in(request, qr_hash):
	if request.method == 'GET':
		return return_checkin_page(request, qr_hash)
	elif request.method == 'POST':
		return perform_checkin(request, qr_hash)
  	
@login_required
def return_checkin_page(request, qr_hash):
	print 'GET %s' % (qr_hash)
	qr = QRTable.objects.get(qr_hash=qr_hash)
	context = {'location': qr.entity_b, 'qr_hash': qr_hash}
  	return render(request, 'quartirs_app/check_in.html', context)

def perform_checkin(request, qr_hash):
	print 'POST %s' % (qr_hash)
	entity_a = request.POST['user']
	qr = QRTable.objects.get(qr_hash = qr_hash)
	print 'a = ', qr.entity_a
	if qr.entity_a != '':
		# QR code has already been used
		return HttpResponse('Code already used, scan a fresh code please')
	qr.entity_a = entity_a
	validUser = ValidatedUsers(entity_a=entity_a, entity_b=qr.entity_b)
	validUser.save()
	qr.save()
	return HttpResponse('You\'ve checked in!')

def authenticate_service(request):
	pass

def generate_qr(request):
	pass
def authenticate_requestor(request):
	pass
def get_validated_users(request):
	pass