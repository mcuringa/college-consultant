from django.db import models
from django import forms
from django.forms import ModelForm

class Major(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ('name',)
        
class Sport(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ('name',)

class School(models.Model):
  state_choices = {('AK', 'Alaska'),
                   ('AL', 'Alabama'),
                   ('AR', 'Arkansas'),
                   ('AZ', 'Arizona'),
                   ('CA', 'California'),
                   ('CO', 'Colorado'),
                   ('CT', 'Connecticut'),
                   ('DE', 'Deleware'),
                   ('FL', 'Florida'),
                   ('GA', 'Georgia'),
                   ('HI', 'Hawaii'),
                   ('IA', 'Iowa'),
                   ('ID', 'Idaho'),
                   ('IL', 'Illinois'),
                   ('IN', 'Indiana'),
                   ('KS', 'Kansas'),
                   ('KY', 'Kentucky'),
                   ('LA', 'Louisiana'),
                   ('MA', 'Massachusetts'),
                   ('MD', 'Maryland'),
                   ('ME', 'Maine'),
                   ('MI', 'Michigan'),
                   ('MN', 'Minnesota'),
                   ('MO', 'Missouri'),
                   ('MS', 'Mississippi'),
                   ('MT', 'Montana'),
                   ('NC', 'North Carolina'),
                   ('ND', 'North Dakota'),
                   ('NE', 'Nebraska'),
                   ('NH', 'New Hampshire'),
                   ('NJ', 'New Jersey'),
                   ('NM', 'New Mexico'),
                   ('NV', 'Nevada'),
                   ('NY', 'New York'),
                   ('OH', 'Ohio'),
                   ('OK', 'Oklahoma'),
                   ('OR', 'Oregon'),
                   ('PA', 'Pennsylvania'),
                   ('RI', 'Rhode Island'),
                   ('SC', 'South Carolina'),
                   ('SD', 'South Dakota'),
                   ('TN', 'Tennessee'),
                   ('TX', 'Texas'),
                   ('UT', 'Utaha'),
                   ('VA', 'Virginia'),
                   ('VT', 'Vermont'),
                   ('WA', 'Washington'),
                   ('WI', 'Wisconsin'),
                   ('WV', 'West Virginia'),
                   ('WY', 'Wyoming'),
                   ('DC', 'Washington, DC')}
  gender_choices = {(1,"Co-ed"),(2,"All Female"),(3,"All Male")}
  name = models.CharField(max_length=500)
  is_four_year = models.BooleanField(default=True)
  is_public = models.BooleanField(default=True)
  school_size = models.IntegerField()
  school_gender = models.IntegerField(choices=gender_choices)
  is_residential = models.BooleanField(default=True)
  location_type = models.IntegerField()
  location_state = models.CharField(choices=state_choices,max_length=2)
  majors = models.ManyToManyField(Major)
  sports = models.ManyToManyField(Sport)
  major_choices = {(1,"Accounting"),
                   (2,"Biology/Biotechnology"),
                   (3,"Business"),
                   (4,"Communication/Journalism"),
                   (5,"Computer Science/Computer Technology"),
                   (6,"Criminal Justice"),
                   (7,"Education"),
                   (8,"Marketing"),
                   (9,"Nursing"),
                   (10,"Political Science/Sociology"),
                   (11,"Psychology/Counseling")}
  major = models.IntegerField(choices=major_choices)
  
class SchoolForm(ModelForm):
    """A ModelForm to hold our schools"""
    class Meta:
        model = School
        
class Contact(models.Model):

  name = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  comments = models.CharField(max_length=500)

class ContactForm(ModelForm):
    class Meta:
        model = Contact


