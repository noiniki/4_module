from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

def index(request):
    advertisement = Advertisement.objects.all()
    context = {'advertisement': advertisement}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')



