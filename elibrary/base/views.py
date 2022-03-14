from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
from .models import Room
from .forms import RoomForm
from .models import Topic
# rooms=[
#     {'id':1,'name':'Lets learn python '},
#     {'id':2,'name':'Lets learn java '},
#     {'id':3,'name':'Lets learn js'},
# ]
def home(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    # this rooms overriding above rooms list 
    # rooms=Room.objects.get()
    # rooms=Room.objects.filter()
    # rooms=Room.objects.exclude()
    rooms_count=rooms.count()
    topics=Topic.objects.all()

    context={'rooms':rooms,'topics':topics,'rooms_count':rooms_count}
    return render(request,"base/base_home.html",context)

def room(request,pk):
    # room=None
    # for i in rooms:
    #     if i['id']==int(pk):
    #         room=i
    room=Room.objects.get(id=pk)
    context={'room':room}

    return render(request,"base/base_room.html",context)

def createRoom(request):
    form=RoomForm()
    if request.method=='POST':
        # print(request.POST)
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}

    return render(request,"base/room_form.html",context)

def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'room':room,'form':form}
    return render(request,"base/room_form.html",context)

def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')

    return render(request,"base/delete.html",{'obj':room})

