from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404


def index(request):
    return render(request, 'main/index.html')