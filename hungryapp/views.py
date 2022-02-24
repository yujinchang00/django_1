from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from .models import Board

# Create your views here.

def home(request):
    board = Board.objects
    return render(request, 'categories.html', {'boards' : board})

def lists(request, board_category):
    boards = Board.objects.filter(category=board_category)
    return render(request, 'lists.html', {'board' : boards})

def detail(request, board_id):
    board_detail=get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board_detail' : board_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    board = Board()
    board.category = request.GET['category']
    board.title = request.GET['title']
    board.points = request.GET['points']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/board/' + str(board.id) + '/')
    
def delete(request, board_id):
    board = Board.objects.get(pk=board_id)
    category = board.category
    board.delete()
    return redirect('/board/' + category + '/')

def edit(request, board_id):
    board_edit = Board.objects.get(pk=board_id)
    return render(request, 'edit.html', {'board' : board_edit})

def update(request, board_id):
    board = Board.objects.get(pk=board_id)
    board.category = request.GET['category']
    board.title = request.GET['title']
    board.points = request.GET['points']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/board/' + str(board.id) + '/')