from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
