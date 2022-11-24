# urls.py in new application

from django.urls import path
from . import views #import views from current folder

urlpatterns = [
    path("", views.index, name="index"), # path to new view
]