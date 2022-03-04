from django.contrib import admin
from .models import Certificate, Course
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
@admin.register(Course)
class CourseAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'created_at']
    list_filter = ['name', 'status']
    search_fields = ['name']


@admin.register(Certificate)
class CertificateAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'familiya', 'ism', 'sharf', 'course', 'start_date', 'end_date', 'month', 'cer_nomer', 'qr_code', 'status']
    list_filter = ['month', ]
    search_fields = ['familiya', 'ism', 'sharf', 'month',]
