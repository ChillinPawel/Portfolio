from django.shortcuts import render

from .models import Comment

def allcomments(request):
    comments = Comment.objects.order_by('-post_date')
    
    if request.method == 'POST':
        user = request.POST.get('user', '')
        content = request.POST.get('content', '')
        comment = Comment(user=user, content=content)
        comment.save()


    return render(request, 'comments/comments.html', {'comments':comments})

def newcomment(request):
    comments = Comment.objects.order_by('-post_date')
    return render(request, 'comments/newcomment.html', {'comments':comments})
