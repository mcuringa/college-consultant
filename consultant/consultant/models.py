from django.db import models
from django import forms
from django.forms import ModelForm

class School(models.Model):

  name = models.CharField(max_length=500)
  four_year_college = models.Boolean(default=True)
  is_public = models.Boolean(default=True)
  population = models.IntergerField()
  gender = models.CharField(max_length=2)
  location = models.IntergerField(default=0)
  zip_code = models.IntergerField(max_length=5)
  state = models.CharField(max_length=2)
  campus_style = models.IntergerField()

class Myth(models.Model):

    myth = models.TextField()
    is_true = models.Boolean()
    correct_count = models.IntergerField()
    wrong_count = models.IntergerField()

class About_Me(models.Model):

    name = models.TextField()
    bio = models.TextField()
