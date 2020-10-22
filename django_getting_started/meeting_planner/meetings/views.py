from django.shortcuts import render,get_object_or_404,redirect
from django.forms import modelform_factory
from meetings.models import Meeting,Room
# Create your views here.

def details(request,id):
    #its is without handling 404 error
    #meeting = Meeting.objects.get(pk=id)
    #handling 404 error
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request,'meetings/details.html',{'meeting':meeting})

def rooms_list(request):
    return render(request,'meetings/rooms_list.html',{'rooms':Room.objects.all()})

MeetingFrom = modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method == 'POST':
        form = MeetingFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')


    else:
        form = MeetingFrom()
    return render(request,'meetings/new.html',{'form':form})