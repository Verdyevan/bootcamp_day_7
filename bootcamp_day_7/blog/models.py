from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    title = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title

class DaftarKuliah(models.Model):
    title = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title