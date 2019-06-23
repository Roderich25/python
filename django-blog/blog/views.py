from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Rodrigo',
        'title': 'My First Post',
        'content': 'Something goes here...',
        'date': 'Jun 21, 2019'
    },
    {
        'author': 'Pablo Rodrigo',
        'title': 'My Second Post',
        'content': 'Something goes here...',
        'date': 'Jun 22, 2019'
    },
    {
        'author': 'Pablo',
        'title': 'My Third Post',
        'content': 'Something goes here...',
        'date': 'Jun 23, 2019'
    }
]


# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
