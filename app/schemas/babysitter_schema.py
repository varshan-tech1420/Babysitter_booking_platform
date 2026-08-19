class BabysitterSchema:
    def __init__(
        self,
        name,
        email,
        phone,
        experience,
        hourly_rate
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.experience = experience
        self.hourly_rate = hourly_rate

    def validate(self):
        if not self.name:
            raise ValueError("Name is required")

        if not self.email:
            raise ValueError("Email is required")

        if not self.phone:
            raise ValueError("Phone is required")

        if self.experience < 0:
            raise ValueError("Experience cannot be negative")

        if self.hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative")

        return True