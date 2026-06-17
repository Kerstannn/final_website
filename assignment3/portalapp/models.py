from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    interest = models.CharField(max_length=100)

    def __str__(self):
        return self.name