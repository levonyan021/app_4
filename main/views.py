from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from .models import *

def index(request):
    element = GalleryModel.objects.order_by('-desc')
    context = {'element':element}
    return render(request, 'main/index.html',context=context)