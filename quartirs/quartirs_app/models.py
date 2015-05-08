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

class ValidatedUsers(models.Model):
  entity_b = models.CharField(max_length=200)
  entity_a = models.CharField(max_length=200)