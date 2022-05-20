from django.shortcuts import render
from .models import Certificate


# Create your views here.
def print_cer(request):
    # persons = Certificate.objects.filter(start_date='25').filter(month="aprel")
    persons = Certificate.objects.filter(cer_nomer__gt=827)
    for p in persons:
        if p.sharf is None:
            p.sharf = ''
            p.save()

    context = {
        "persons": persons,
    }
    return render(request, 'certificate_print.html', context)
