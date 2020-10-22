from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    try:
        return render(request,"website/welcome.html",
                  {'meetings': Meeting.objects.all()})
    except:
        return HttpResponse("Page not found")

def date(request):
    return HttpResponse("The page server at {0}".format(str(datetime.now())))

def about(request):
    return HttpResponse("I'm mani here for learning django framework")