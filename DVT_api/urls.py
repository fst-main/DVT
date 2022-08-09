from django.contrib import admin
from django.urls import path
#from DVT_api.views import UserItemViews
from .views import get_user, login
from .views import post_user



urlpatterns = [
    path('api/login', login),
    path('get_user/', get_user),
    path('post_user/', post_user),
    #path('user-items/<int:id>', UserItemViews.as_view()),
]