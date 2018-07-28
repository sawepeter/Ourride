from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Board


def home(request):
    baords = Board.objects.all()
    return render(request, 'home.html', {'baords':baords})

def baords_topics(request, pk):
    baords = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'baords':baords})


