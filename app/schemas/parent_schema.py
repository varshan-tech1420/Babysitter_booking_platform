class ParentSchema:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def validate(self):
        if not self.name:
            raise ValueError("Name is required")

        if not self.email:
            raise ValueError("Email is required")

        if not self.phone:
            raise ValueError("Phone is required")

        if not self.address:
            raise ValueError("Address is required")

        return True