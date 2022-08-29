from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'chat/home.html', context)

def delete_chat(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()
    return redirect('forum')

def input_name(request, pk):
    chat = Room.objects.get(pk=pk)
    context = {
        'room': chat,
    }
    return render(request, 'chat/input_name.html', context)

def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']
    room = Room.objects.filter(name=room_name)
    if room.exists():
        return redirect(str(room[0].id)+'-chat/?username='+username)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect(str(new_room.id)+'-chat/?username='+username)

def room(request, pk):
    username = request.GET.get('username')
    room_details = Room.objects.get(pk=pk)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': str(room_details.id),
        'room_details': room_details
    })

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, pk):
    room_details = Room.objects.get(pk=pk)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
