from unicodedata import name
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    coach = models.CharField(max_length=150)

    class meta:
        ordering = ["name"]
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name.upper()
