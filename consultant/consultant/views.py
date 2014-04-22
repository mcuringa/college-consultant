from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from consultant.models import *

    
# def home(request):
    # """The about us link"""
    
    # majors = {"education":  ("Adelphi", "Molloy", "Queens"), "psychology": ()}
    
    # context = {}
    
    # if majors == "education":
        # context[key] = value
        
    # return render(request, 'home.html')

def college_form(request):
    """Enter a new college"""
    
    return render(request, 'school_survey_admin.html')
    
# def college_search(request):
    # """The search link"""
    
    # return render(request, 'school_survey.html')
    
# def contact_us(request):
    # """The contact us link"""
    
    # return render(request, 'contact_us.html')
    
    
def save_school(request):


    form = SchoolForm(request.POST)
    school = form.save()

    # send them to the home page after saving
    # this will call views.home() from above
    return HttpResponseRedirect("/")


