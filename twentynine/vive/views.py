from django.shortcuts import render
# Create your views here.

tweet=[
    {'name':'Prince Raj',
     'age':20,
     'city':'Madhubani'},
    {'name':'Shashank',
     'age':21,
     'city':'Muzzafarpur'},
    {'name':'Mohak',
     'age':19,
     'city':'Rohtas'},
    {'name':'Umang Niranjan',
     'age':21,
     'city':'Jhanshi'}
]

def home(request):
    context={
        'posts':tweet,
        'title':'Home'
    }
    return render(request,'vive/home.html',context)

def about(request):
    return render(request,'vive/about.html',{'title':'About'})