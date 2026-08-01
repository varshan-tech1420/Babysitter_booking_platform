from django.db import models
from booking.models import Booking

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.payment_status