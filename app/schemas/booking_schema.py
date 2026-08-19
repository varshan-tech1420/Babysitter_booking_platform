class BookingSchema:
    def __init__(
        self,
        parent_id,
        babysitter_id,
        booking_date,
        start_time,
        end_time,
        status="pending"
    ):
        self.parent_id = parent_id
        self.babysitter_id = babysitter_id
        self.booking_date = booking_date
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def validate(self):
        if not self.parent_id:
            raise ValueError("Parent is required")

        if not self.babysitter_id:
            raise ValueError("Babysitter is required")

        if not self.booking_date:
            raise ValueError("Booking date is required")

        if not self.start_time:
            raise ValueError("Start time is required")

        if not self.end_time:
            raise ValueError("End time is required")

        allowed_status = [
            "pending",
            "confirmed",
            "completed",
            "cancelled"
        ]

        if self.status not in allowed_status:
            raise ValueError("Invalid booking status")

        if self.end_time <= self.start_time:
            raise ValueError("End time must be after start time")

        return True