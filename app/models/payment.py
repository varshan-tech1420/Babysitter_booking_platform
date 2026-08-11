from django.db import models
from app.models.booking import Booking


class Payment(models.Model):
    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("paid", "Paid"),
            ("failed", "Failed"),
        ],
        default="pending"
    )

    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment - {self.booking.id}"