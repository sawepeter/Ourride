from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Board


def home(request):
    baords = Board.objects.all()
    return render(request, 'home.html', {'baords':baords})

def baords_topics(request, pk):
    baords = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'baords':baords})


