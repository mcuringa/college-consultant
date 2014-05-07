from django.db import models
from django import forms
from django.forms import ModelForm

class School(models.Model):

  name = models.CharField(max_length=500)
  is_four_year = models.BooleanField(default=True)
  is_public = models.BooleanField(default=True)
  #school_size = models.IntergerField()
  # gender = models.CharField(max_length=6)
  # location = models.IntergerField(default=0)
  # resident = models.BooleanField(default=True)
  # zip_code = models.IntergerField(max_length=5)
  # state = models.CharField(max_length=2)

class SchoolForm(ModelForm):
    """A ModelForm to hold our schools"""
    class Meta:
        model = School
		
class Contact(models.Model):

  name = models.CharField(max_length=50)
  email = models.EmailField()
  comments = models.ChartField(max_length=500)

class ContactForm(ModelForm):
    class Meta:
        model = Contact


