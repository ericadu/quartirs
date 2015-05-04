from django.db import models

# Create your models here.
class QRTable(models.Model):
	entity_b = models.CharField(max_length=200)
	qr_hash = models.CharField(max_length=100)
	entity_a = models.CharField(max_length=200)

class ValidatedUsers(models.Model):
	entity_b = models.CharField(max_length=200)
	entity_a = models.CharField(max_length=200)