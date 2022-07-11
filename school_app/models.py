from django.db import models


class School(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=255)
    phone_numbers = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
