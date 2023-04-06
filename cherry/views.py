from django.shortcuts import render
from cherry.models import *
# Create your views here.
from django.db.models.functions import Length
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='Cricket')
    #LOW=Webpage.objects.get(topic_name='Chess')
    LOW=Webpage.objects.exclude(topic_name='Cricket')
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.all().order_by('name')
    #LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)


def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-07-10')
    LOA=AccessRecord.objects.filter(date__gte='2022-07-10')
    LOA=AccessRecord.objects.filter(date__lt='2022-07-10')
    LOA=AccessRecord.objects.filter(date__lte='2022-07-10')
    d={'accessrecords':LOA}
    return render(request,'display_access.html',d)
