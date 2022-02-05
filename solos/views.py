from django.http import HttpResponse
from django.shortcuts import render
from .models import Solo

# Create your views here.
def index(request):
    context = {'solos': None}

    if request.GET.keys():
        solo_query = Solo.objects.all()

        if request.GET.get('instrument', None):
            solo_query = Solo.objects.filter(
                instrument=request.GET.get('instrument', None)
            )
        if request.GET.get('artist', None):
            solo_query = solo_query.filter(
                artist=request.GET.get('artist', None)
            )
        context['solos'] = solo_query

    return render(request, 'solos/index.html', context)