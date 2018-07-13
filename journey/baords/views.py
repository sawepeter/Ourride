from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Board


def home(request):
    baords = Board.objects.all()
    baords_names = list()

    for board in baords:
        baords_names.append(board.name)

    response_html = '<br>'.join(baords_names)

    return HttpResponse(response_html)
