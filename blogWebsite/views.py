from django.http import HttpResponse
from django.shortcuts import render
 
    
def home(request):
    return render(request, "home.html")
   #return HttpResponse('This is the home page ')

def about(request):
    return render(request, "about.html")
    #return HttpResponse('This is About page')