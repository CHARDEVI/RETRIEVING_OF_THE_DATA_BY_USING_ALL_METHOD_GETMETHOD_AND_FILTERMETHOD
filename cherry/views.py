from django.shortcuts import render
from cherry.models import *
# Create your views here.
from django.db.models.functions import Length
from django.db.models import Q
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
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.exclude(topic_name='Sports')
    LOW=Webpage.objects.all()


    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.order_by(Length('name').desc())
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='D')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__endswith='i')
    LOW=Webpage.objects.all()

    LOW=Webpage.objects.filter(name__contains='o')
    LOW=Webpage.objects.filter(name__in=('Devi','Dhoni'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{5}')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(Q(topic_name='Cricket')& Q(name='Dhoni'))
    LOW=Webpage.objects.filter(Q(topic_name='Cricket'))
    LOW=Webpage.objects.all()


    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)






def display_update(request):
    LOU=Webpage.objects.all()

    
    d={'webpages':LOU}
    LOU=Webpage.objects.filter(name='MSD').update(url='https://M S Dhoni.com')
    LOU=Webpage.objects.filter(name='Devi').update(url='https://Charishma.com')
    LOU=Webpage.objects.filter(topic_name='Volly Ball').update(name='surya')
    LOU=Webpage.objects.all().update(url='https://Cherry.com')


    TO=Topic.objects.get(topic_name='Cricket')
    LOU=Webpage.objects.update_or_create(name='chardevi',defaults={'topic_name':TO,'url':'https://chardevi.com'})

def display_delete(request):
    LOD=Webpage.objects.all()

    d={'webpages':LOD}
    LOD=Webpage.objects.filter(name='surya').delete()
    LOD=Webpage.objects.filter(name='Vivek').delete()



    LOD=Webpage.objects.all().delete()



    return render(request,'display_webpage.html',d)



def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-07-10')
    LOA=AccessRecord.objects.filter(date__gte='2022-07-10')
    LOA=AccessRecord.objects.filter(date__lt='2022-07-10')
    LOA=AccessRecord.objects.filter(date__lte='2022-07-10')
    LOA=AccessRecord.objects.all()


    d={'accessrecords':LOA}
    return render(request,'display_access.html',d)
