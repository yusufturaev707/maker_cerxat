from django.urls import path, include
from django.views.generic import TemplateView

from .views import print_cer

urlpatterns = [
    path('', print_cer, name='print'),
]
