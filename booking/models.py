from django.db import models
from parents.models import Parent
from babysitters.models import Babysitter

class Booking(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    babysitter = models.ForeignKey(Babysitter, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.parent.name} - {self.babysitter.name}"