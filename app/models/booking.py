from django.db import models
from app.models.parent import Parent
from app.models.babysitter import Babysitter


class Booking(models.Model):
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    babysitter = models.ForeignKey(
        Babysitter,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="pending"
    )

    def __str__(self):
        return f"{self.parent.name} - {self.babysitter.name}"