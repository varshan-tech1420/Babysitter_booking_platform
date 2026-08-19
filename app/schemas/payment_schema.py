class PaymentSchema:
    def __init__(self, booking_id, amount, payment_status="pending"):
        self.booking_id = booking_id
        self.amount = amount
        self.payment_status = payment_status

    def validate(self):
        if not self.booking_id:
            raise ValueError("Booking is required")

        if self.amount is None or self.amount < 0:
            raise ValueError("Amount cannot be negative")

        allowed_status = [
            "pending",
            "paid",
            "failed"
        ]

        if self.payment_status not in allowed_status:
            raise ValueError("Invalid payment status")

        return True