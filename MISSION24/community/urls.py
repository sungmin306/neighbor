from django.contrib import admin
from django.urls import path, include
#from .views import SignUp, SignIn
from . import views
urlpatterns = [
    path('home/',views.home),
    #path('SignUp/',views.SignUp.as_view(), name='SignUp'),
    path('SignUp/',views.SignUp, name='SignUp'),
    #path('SignIn/',views.SignIn.as_view(), name='SignIn'),
    path('SignIn/',views.SignIn, name='SignIn'),
    path('quick/',views.CreatepostsViews)
    #path('list/',views.CreatePostsView.as_view())
]
