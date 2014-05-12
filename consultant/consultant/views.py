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
    return render(request, "school_survey.html")
    
def search(request):
    """The search link"""
    search_params=request.POST
    schools=School.objects.all()
    
    year_param = int(search_params.get("is_four_year", 3))
    if year_param == 1:
        schools = schools.filter(is_four_year=True)
    if year_param == 2:
        schools = schools.filter(is_four_year=False)
    
    public_param = int(search_params.get("is_public", 3))
    if public_param == 1:
        schools = schools.filter(is_public=True)
    if public_param == 2:
        schools = schools.filter(is_public=False)
    
    gender_params = int(search_params.get("school_gender", 1))
    if gender_params == 1:
        schools = schools.filter(school_gender=1)
    if gender_params == 2:
        schools = schools.filter(school_gender=2)
    if gender_params == 3:
        schools = schools.filter(school_gender=3)   
    
    major_ids = []
    majors = search_params.get("majors", [])
    for major_id in majors:
        major_ids.extend(int(major_id))
    if majors:
        schools = schools.filter(majors__in=major_ids)
    
    context = { "schools": schools }
    
    return render(request, 'search_results.html', context)
    
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


