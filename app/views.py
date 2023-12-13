from django.shortcuts import render
from app.models import *
# Create your views here.

def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topics' : QLTO}
    return render(request,'display_topics.html',d)

def display_web(request):
    QLWO=Webpage.objects.all()
    d={'web' : QLWO}
    return render(request,'display_web.html',d)

def display_asrecords(request):
    QLAO=AccessRecord.objects.all()
    d={'ar' : QLAO}
    return render(request,'display_asrecords.html',d)
