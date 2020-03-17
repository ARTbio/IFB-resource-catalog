from django.db import models

class Credit(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    laboratory = models.CharField(max_length=1000)
    institute = models.CharField(max_length=1000)
    adress = models.CharField(max_length=1000, null=True)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.name
