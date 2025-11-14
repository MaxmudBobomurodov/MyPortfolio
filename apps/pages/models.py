from django.db import models


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    job_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    location = models.CharField(max_length=100)
    summary = models.TextField()
    technical_skills = models.CharField(max_length=100)

class Skills(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField()

class ProfessionalSkills(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField()

class Education(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    summary = models.TextField()

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
