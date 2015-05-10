from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.template import RequestContext, loader

from quartirs_app.models import QRTable, ValidatedUsers

from hashlib import sha256
from random import getrandbits

# Create your views here.
@login_required(login_url='/6857/accounts/login/')
def index(request):
	return render(request, 'quartirs_app/index.html', {})

@login_required(login_url='/6857/accounts/login/')
def check_in(request, qr_hash):
	if request.method == 'GET':
		return return_checkin_page(request, qr_hash)
	elif request.method == 'POST':
		return perform_checkin(request, qr_hash)
  	

def return_checkin_page(request, qr_hash):
	qr = QRTable.objects.get(qr_hash=qr_hash)
	context = {'location': qr.entity_b, 'qr_hash': qr_hash}
  	return render(request, 'quartirs_app/check_in.html', context)

def perform_checkin(request, qr_hash):
	entity_a = request.POST['user']
	qr = QRTable.objects.get(qr_hash = qr_hash)
	if qr.entity_a != '':
		# QR code has already been used
		return HttpResponse('Code already used, scan a fresh code please')
	qr.entity_a = entity_a
	validUser = ValidatedUsers(entity_a=entity_a, entity_b=qr.entity_b)
	validUser.save()
	qr.save()
	return HttpResponse('You\'ve checked in!')

@login_required(login_url='/6857/accounts/login/')
def generate_qr(request):
	context = {}
	qr_hash = sha256(str(getrandbits(256))).hexdigest()

	# Save Hash
	qr = QRTable.objects.create_qr(request.user.username, qr_hash)
	
	context['qr_url'] = request.build_absolute_uri() + str(qr_hash)
	context['qr_hash'] = qr_hash
	return render(request, 'quartirs_app/index.html', context)

@login_required(login_url='/6857/accounts/login/')
def get_validated_users(request):
	validUsers = ValidatedUsers.objects.filter(entity_b=request.user.username).order_by('-check_in_time')
	# format time and change timezone to eastern
	validUsers = [{'entity_a': u.entity_a, 'entity_b':u.entity_b, 'check_in_time': u.check_in_time_formatted} for u in validUsers.all()]
	return render(request, 'quartirs_app/user_list.html', { 'validUsers': validUsers})

@login_required(login_url='/6857/accounts/login/')
def test_qr(request, qr_hash):
	# check if qr_hash was made by logged in user
	try: 
		qr = QRTable.objects.get(qr_hash=qr_hash, entity_b=request.user.username)
	except QRTable.DoesNotExist:
		raise Http404('No QR code found for that hash and your username')
	print qr
	if qr.entity_a != '':
		print 'returning true'
		return HttpResponse(True)
	print 'returning false'
	return HttpResponse(False)

@login_required(login_url='/6857/accounts/login/')
def get_validated_users_table(request):
	validUsers = ValidatedUsers.objects.filter(entity_b=request.user.username).order_by('-check_in_time')
	# format time and change timezone to eastern
	validUsers = [{'entity_a': u.entity_a, 'entity_b':u.entity_b, 'check_in_time': u.check_in_time_formatted} for u in validUsers.all()]
	return render(request, 'quartirs_app/user_table.html', { 'validUsers': validUsers })
