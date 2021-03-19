from django.urls import path

from . import views

urlpatterns = [
    path('', views.allcomments, name='comments'),
    path('newcomment/', views.newcomment, name='newcomment'),
]
