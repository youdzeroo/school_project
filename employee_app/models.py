from django.db import models
from courses_app.models import Course


class Employers:
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    M = 'Male'
    F = 'Female'
    GENDER = [
        (M, 'Male'),
        (F, 'Female')
    ]
    gender = models.CharField(max_length=6, choices=GENDER)
    course = models.ManyToManyField(Course)
