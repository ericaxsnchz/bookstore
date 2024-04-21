from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book

def index(request):
    return render(request, 'template.html')

def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'store.html', context)

def login(request):
    return render(request, 'login.html')

@login_required
def store(request):
    return render(request, 'store.html')