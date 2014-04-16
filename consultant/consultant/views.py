from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#def save_school(request):
    

def home(request):
    """The about us link"""
    
    majors = {"education":  ("Adelphi", "Molloy", "Queens"), "psychology": ()}
    
    context = {}
    
    if majors == "education":
        context[key] = value
        
    return render(request, 'home.html')

def college_form(request):
    """Enter a new college"""
    
    return render(request, 'school_survey_admin.html')
    
def college_search(request):
    """The search link"""
    
    return render(request, 'college_search.html')
    

def common_myths(request):
    """The quick facts link"""
    
    return render(request, 'common_myths.html')   

 
    
def about_us(request):
    """The about us link"""
    
    return render(request, 'about_us.html')
    
    
def contact_us(request):
    """The contact us link"""
    
    return render(request, 'contact_us.html')
    
    
    #return render(request, 'save_school.html')


