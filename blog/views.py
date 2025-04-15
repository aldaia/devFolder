from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def indexV(request):
    return render(request, 'blog/index.html')

def oneV(request):
    return render(request, 'blog/one.html')

def twoV(request):
    return render(request, 'blog/two.html')
