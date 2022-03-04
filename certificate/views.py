from django.shortcuts import render
from .models import Certificate


# Create your views here.
def print_cer(request):
    persons = Certificate.objects.filter(start_date='21').filter(month="fevral")

    context = {
        "persons": persons,
    }
    return render(request, 'certificate_print.html', context)
