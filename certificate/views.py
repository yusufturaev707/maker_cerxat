from django.shortcuts import render
from .models import Certificate


# Create your views here.
def print_cer(request):
    persons = Certificate.objects.all()

    context = {
        "persons": persons,
    }
    return render(request, 'certificate_print.html', context)
