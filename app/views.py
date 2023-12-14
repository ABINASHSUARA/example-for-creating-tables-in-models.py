from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
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

def insert_topic(request):
    tn=input("insert the topic name : ")
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def insert_webpage(request):
    tn=input("enter the topic name:")
    n=input('enter the name:')
    u=input('enter the url:')
    e=input('enter the email:')

    TO=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()

    QLWO=Webpage.objects.all()
    d={'web' : QLWO}
    return render(request,'display_web.html',d)



    
def insert_asrecords(request):
    pk=int(input("enter pk value of webpage:"))
    d=input("enter the date:")
    a=input("enter the author name:")

    wo=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    NAO.save()

    QLAO=AccessRecord.objects.all()
    d={'ar' : QLAO}
    return render(request,'display_asrecords.html',d)

   