from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    """The home page"""
        
    return render(request, 'home.html')
