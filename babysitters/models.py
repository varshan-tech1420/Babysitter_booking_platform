from django.db import models

class Babysitter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    experience = models.IntegerField()
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name