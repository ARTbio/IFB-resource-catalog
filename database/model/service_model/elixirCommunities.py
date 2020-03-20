from django.db import models

class ElixirCommunities(models.Model):
    name = models.CharField(max_length=10000)
    class Meta:
        verbose_name_plural = "Elixir Communities"

    def __str__(self):
        return self.name
