from django.contrib import admin

# Register your models here.
from .models import Mahasiswa, DaftarKuliah

admin.site.register(Mahasiswa)
admin.site.register(DaftarKuliah)
