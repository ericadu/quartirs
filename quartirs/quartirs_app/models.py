from django.db import models

class QRTableManager(models.Manager):
  def create_qr(self, qr_hash):
    qr = self.create(qr_hash=qr_hash)
    return qr

# Create your models here.
class QRTable(models.Model):
  entity_b = models.CharField(max_length=200)
  qr_hash = models.CharField(max_length=100)
  entity_a = models.CharField(max_length=200)
  objects = QRTableManager()

	def __unicode__(self):
		return self.entity_a + ' checked in with ' + self.entity_b + ' using QR ' + self.qr_hash

class ValidatedUsers(models.Model):
	entity_b = models.CharField(max_length=200)
	entity_a = models.CharField(max_length=200)
	check_in_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.entity_a + ' is validated with ' + self.entity_b
