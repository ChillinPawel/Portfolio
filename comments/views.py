from django.shortcuts import render

from .models import Comment

def allcomments(request):
    comments = Comment.objects
    return render(request, 'comments/comments.html', {'comments':comments})

