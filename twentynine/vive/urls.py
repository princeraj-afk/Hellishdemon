from django.urls import path
from . import views


urlpatterns = [
    path('admin/', views.home(), name="vive-home"),
]