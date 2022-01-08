from django.contrib import admin
from .models import Certificate
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
@admin.register(Certificate)
class CertificateAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'familiya', 'ism', 'sharf', 'kurs_kuni', 'cer_nomer', 'qr_code']
    list_filter = ['kurs_kuni', ]
    search_fields = ['familiya', 'ism', 'sharf', 'kurs_kuni',]
