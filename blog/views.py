from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Games

def game_list(request):
    games = Games.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'blog/game_list.html', {'games':games})

def game_detail(request, pk):
    # request to model 
    game = get_object_or_404(Games, pk=pk)
    # render template game_detail with delivery data from model
    return render(request, 'blog/game_detail.html', {'game':game})
