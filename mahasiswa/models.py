from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    foto = models.CharField(max_length=500, null=True)


    def _str_(self):
        return "{}".format(self.nama)