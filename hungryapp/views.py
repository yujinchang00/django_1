from django.shortcuts import get_object_or_404, render
from .models import Board

# Create your views here.

def home(request):
    board = Board.objects
    return render(request, 'home.html', {'board' : board})

def detail(request, board_id):
    board_detail=get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board_detail' : board_detail})