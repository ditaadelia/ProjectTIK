from django.db import models

# Create your models here.

class Tendik(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)