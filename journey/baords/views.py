from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from .models import Board


def home(request):
    baords = Board.objects.all()
    return render(request, 'home.html', {'baords':baords})

def baords_topics(request, pk):
    try:
        baords = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'baords':baords})


