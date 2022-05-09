from django.shortcuts import render
from django.utils import timezone
from .models import Games

def game_list(request):
    games = Games.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'blog/game_list.html', {'games':games})
