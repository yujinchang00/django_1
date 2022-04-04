from django.shortcuts import render
from .models import Index

# Create your views here.
def home(request):
    rate = Index.objects
    return render(request, 'index.html', {'rates' : rate})