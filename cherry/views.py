from django.shortcuts import render
from cherry.models import *
# Create your views here.

def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)


def display_access(request):
    LOA=AccessRecord.objects.all()
    d={'accessrecords':LOA}
    return render(request,'display_access.html',d)
