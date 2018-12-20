from django.http import HttpResponse
from django.shortcuts import render
from.models import Post

def home(request):
    context = {

        'posts': Post.objects.all()
    }
    return render(request, 'BlogApp/home.html', context)

def about(request):
    return render(request, 'BlogApp/about.html',   {'title': 'About'})
