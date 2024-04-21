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
    return render(request, 'base.html', context)