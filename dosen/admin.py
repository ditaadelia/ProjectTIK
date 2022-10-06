from django.contrib import admin
from dosen.models import Dosen

# Register your models here.

class DosenAdmin(admin.ModelAdmin):
    list_display = ['nidn', 'nip', 'nama', 'jabatan', 'email', 'foto']
    search_fields = ['nip', 'nama']

admin.site.register(Dosen, DosenAdmin)