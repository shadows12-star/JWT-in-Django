from django.contrib import admin
from django.urls import include, path

from .views import posts


urlpatterns = [
   path('post/', posts,name='posts'),
]
