from django.shortcuts import render
from .models import Certificate


# Create your views here.
def print_cer(request):
    persons = Certificate.objects.filter(start_date='18').filter(month="iyul")
    # persons = Certificate.objects.filter(cer_nomer=532)
    for p in persons:
        if p.sharf is None:
            p.sharf = ''
            p.save()

    context = {
        "persons": persons,
    }
    return render(request, 'certificate_print.html', context)
