import requests

from django.shortcuts import render, redirect
from django.conf import settings

from .models import Comment

def allcomments(request):
    comments = Comment.objects.order_by('-post_date')
        
    return render(request, 'comments/comments.html', {'comments':comments})

def newcomment(request):
    comments = Comment.objects.order_by('-post_date')

    return render(request, 'comments/newcomment.html', {'comments':comments,})
