from django.db import models

# Create your models here.

class Dosen(models.Model):
    nidn = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50)
    foto = models.CharField(max_length=500, null=True)


    def _str_(self):
        return "{}".format(self.nama)