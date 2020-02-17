from django.db import models


class Certificat(models.Model):
    name = models.CharField(max_length=10000)
    def __str__(self):
        return self.name
