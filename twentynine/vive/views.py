from django.shortcuts import render
from .models import Friend



def home(request):
    context={
        'friends':Friend.objects.all(),
        'title':'Home'
    }
    return render(request,'vive/home.html',context)

def about(request):
    return render(request,'vive/about.html',{'title':'About'})
