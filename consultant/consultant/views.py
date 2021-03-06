from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from consultant.models import *

    
def home(request):
    """The about us link"""
        
    return render(request, 'home.html')

def college_form(request):
    """Enter a new college"""
    form = SchoolForm()
    schools = School.objects.all()
    context = {"schools": schools, "school": form}
    
    return render(request, 'school_survey_admin.html', context)

def college_search(request):
    form = SchoolForm()
    context = {"school": form}
    return render(request, "school_survey.html", context)
    
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
    
    size_param = int(search_params.get("school_size", 4))
    if size_param == 1:
        schools = schools.filter(school_size__lt=2000)
    if size_param == 2:
        schools = schools.filter(school_size__lte=15000).filter(school_size__gte=2000)
    if size_param == 3:
        schools = schools.filter(school_size__gt=15000)
    
    if search_params.get("school_gender", 1) == "":
        gender_params = 4
    else:
        gender_params = int(search_params.get("school_gender", 4))
    if gender_params == 1:
        schools = schools.filter(school_gender=1)
    if gender_params == 2:
        schools = schools.filter(school_gender=2)
    if gender_params == 3:
        schools = schools.filter(school_gender=3)  
        
    state = search_params.get("location_state", "")
    if state != "":
        schools = schools.filter(location_state=state)
    print(str(schools) + str(type(schools)))
        
    campus_param = int(search_params.get("is_residential", 3))
    if campus_param == 1:
        schools = schools.filter(is_residential=True)
    if campus_param == 2:
        schools = schools.filter(is_residential=False)
        
    location_param = int(search_params.get("location_type", 4))
    if location_param == 1:
        schools = schools.filter(location_type=1)
    if location_param == 2:
        schools = schools.filter(location_type=2)
    if location_param == 3:
        schools = schools.filter(location_type=3)
    print(str(schools) + str(type(schools)) )
    major = int(search_params.get("majors", 0))
    print(str(major))
    if major > 0:
        major_list = [major]
        schools = schools.filter(majors__in=major_list)
    print(str(schools) + str(type(schools)) )
    sport = int(search_params.get("sports", 0))
    if sport > 0:
        sport_list = [sport]
        schools = schools.filter(sports__in=sport_list)
    
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


