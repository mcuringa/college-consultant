from django.db import models
from django import forms
from django.forms import ModelForm

class School(models.Model):

  name = models.CharField(max_length=500)
  is_four_year = models.BooleanField(default=True)
  is_public = models.BooleanField(default=True)
  school_size = models.IntegerField()
  school_gender = models.IntegerField()
  is_residential = models.BooleanField(default=True)
  location_type = models.IntegerField()
  location_state = models.CharField(max_length=500)
  majors = models.IntegerField()
class SchoolForm(ModelForm):
    """A ModelForm to hold our schools"""
    class Meta:
        model = School
		
class Contact(models.Model):

  name = models.CharField(max_length=20)
  email = models.ChartField(max_length=50)
  comments = models.ChartField(max_length=500)

class ContactForm(ModelForm):
    class Meta:
        model = Contact


