from django.db import models
from django import forms
from django.forms import ModelForm

class School(models.Model):

  name = models.CharField(max_length=500)
  four_year_college = models.Boolean(default=true)
  is_public = models.Boolean(default=true)
  population = models.IntergerField()
  gender = models.CharField(max_length=2)
  location = models.IntergerField(default=0)
  zip_code = models.IntergerField(max_length=5)
  state = models.CharField(max_length=2)
  campus_style = models.IntergerField()
