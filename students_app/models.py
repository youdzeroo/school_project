from django.db import models
from courses_app.models import Course


class Student(models.Model):
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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['first_name']
        unique_together = (
                "first_name",
                "last_name",
                "date_of_birth",
                "phone_number"
        )

    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Student, self).save(*args, **kwargs)

    # def save(self):
    #     self.first_name = self.first_name.capitalize()
    #     self.last_name = self.last_name.capitalize()

    def __str__(self):
        return self.first_name
