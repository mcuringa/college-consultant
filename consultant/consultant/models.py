from django.db import models
from django import forms
from django.forms import ModelForm

class School(models.Model):

  name = models.CharField(max_length=500)
  is_four_year = models.BooleanField(default=True)
  # is_public = models.BooleanField(default=True)
  # population = models.IntergerField()
  # gender = models.CharField(max_length=6)
  # location = models.IntergerField(default=0)
  # resident = models.BooleanField(default=True)
  # zip_code = models.IntergerField(max_length=5)
  # state = models.CharField(max_length=2)

class SchoolForm(ModelForm):
    """A ModelForm to hold our schools"""
    class Meta:
        model = School



