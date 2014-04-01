from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    """The home page"""
        
    return render(request, 'home.html')
    

def link1(request):
    """The first test link"""
    
    return render(request, 'link1.html')
    

def link2(request):
    """The second test link"""
    
    return render(request, 'link2.html')
    
    
def link3(request):
    """The third test link"""
    
    return render(request, 'link3.html')
    
    
def link4(request):
    """The fourth test link"""
    
    return render(request, 'link4.html')
