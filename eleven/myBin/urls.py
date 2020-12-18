from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='bin-home'),
    path('about/', views.about,name='bin-about'),
]