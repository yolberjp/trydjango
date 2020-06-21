from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Yolber P',
        'title': 'Blog post',
        'content': 'First post content',
        'date_posted': 'June 21, 2020'
    },
    {
        'author': 'Matias C',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'June 21, 2020'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

