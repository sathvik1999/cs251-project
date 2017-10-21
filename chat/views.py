from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
import itertools
from django.contrib.auth.models import User



@login_required
def chat(request,pk1,pk2):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    room,created=Room.objects.get_or_create(owner=User.objects.get(pk=pk1),opponent=User.objects.get(pk=pk2),title='chat')
    #rooms = Room.objects.get(owner=User.objects.get(pk=pk1),opponent=User.objects.get(pk=pk2))
    #rooms2 = Room.objects.filter(opponent =request.user)
    #rooms = itertools.chain(rooms1, rooms2)
    
    # Render that in the index template

    
    return render(request, "index.html", {"room": room})

def messages(request,pk):
    rooms1=Room.objects.filter(opponent=request.user)
    rooms2=Room.objects.filter(owner=request.user)
    rooms=itertools.chain(rooms1,rooms2)
    return render(request,"messages.html",{"rooms":rooms})
    