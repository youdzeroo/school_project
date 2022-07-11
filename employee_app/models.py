from django.db import models

import school_app.models


class Department(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    school = models.ForeignKey(school_app.models.School, on_delete=models.CASCADE)
    # position = models.ForeignKey(Position, )


class Position(models.Model):
    name = models.CharField(max_length=45)
    duration = models.DateField()
    is_active = models.BooleanField()
    description = models.TextField()
    permission = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Employers(models.Model):
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
    salary = models.IntegerField()
    position = models.ForeignKey(Position, on_delete= models.CASCADE)





