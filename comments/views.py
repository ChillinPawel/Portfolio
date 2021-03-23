import requests
from django.shortcuts import render, redirect
from django.contrib import messages

from django.conf import settings
from .models import Comment

def allcomments(request):
    comments = Comment.objects.order_by('-post_date')

    if request.method == 'POST':
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret' : settings.RECAPTCHA_PRIVATE_KEY,
            'response' :  recaptcha_response
        }
        response = requests.get(url, params=values, verify=True).json().get("success", False)
        ''' End reCAPTCHA validation '''

        if response:
            user = request.POST.get('user')
            content = request.POST.get('content')
            comment = Comment(user=user, content=content)
            comment.save()
            messages.success(request, 'Comment added.')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('newcomment')
        
    return render(request, 'comments/comments.html', {'comments':comments})


def newcomment(request):
    comments = Comment.objects.order_by('-post_date')

    return render(request, 'comments/newcomment.html', {'comments':comments, 'site_key': settings.RECAPTCHA_PUBLIC_KEY})
