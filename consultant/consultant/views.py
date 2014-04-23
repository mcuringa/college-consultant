from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from consultant.models import *

    
def home(request):
    """The about us link"""
        
    return render(request, 'home.html')

def college_form(request):
    """Enter a new college"""
    schools = School.objects.all()
    context = {"schools": schools}
    
    return render(request, 'school_survey_admin.html', context)
    
def college_search(request):
    """The search link"""
    
    return render(request, 'school_survey.html')
    
def contact_us(request):
    """The contact us link"""
    
    return render(request, 'contact_us.html')
    
def common_myths(request):
    """The myths link"""
    
    return render(request, 'common_myths.html')

def about_us(request):
    """The about us link"""
    
    return render(request, 'about_us.html')
    
def save_school(request):


    form = SchoolForm(request.POST)
    school = form.save()

    # send them to the home page after saving
    # this will call views.home() from above
    return HttpResponseRedirect("/new_college")


