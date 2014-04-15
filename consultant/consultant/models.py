from django.db import models
from django import forms
from django.forms import ModelForm

class School(models.Model):

  name = models.CharField(max_length=500)
  four_year_college = models.Boolean(default=True)
  is_public = models.Boolean(default=True)
  population = models.IntergerField()
  gender = models.CharField(max_length=6)
  location = models.IntergerField(default=0)
  resident = models.Boolean(default=True)
  zip_code = models.IntergerField(max_length=5)
  state = models.CharField(max_length=2)

class Facts(models.Model):

<<<<<<< HEAD
	fact = models.TextField()
	is_true = models.Boolean(default=True)
	correct_count = models.IntergerField()
	wrong_count = models.IntergerField()

class About_Me(models.Model):

  name = models.TextField()
  school_attended = models.TextField()
  bio = models.TextField()
=======
    myth = models.TextField()
    is_true = models.Boolean()
    correct_count = models.IntergerField()
    wrong_count = models.IntergerField()

class About_Me(models.Model):

    name = models.TextField()
    bio = models.TextField()
>>>>>>> FETCH_HEAD
