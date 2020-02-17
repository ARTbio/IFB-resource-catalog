from django.db import models


class People(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
