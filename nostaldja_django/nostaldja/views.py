from django.shortcuts import render
from .models import Decade, Fad

# Create your views here.

def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/templates/decade_list.html', {'decades': decades})

def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/templates/fad_list.html', {'fads': fads})

