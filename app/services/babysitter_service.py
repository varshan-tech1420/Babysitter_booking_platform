from app.models.babysitter import Babysitter


def create_babysitter(name, email, phone, experience, hourly_rate):
    return Babysitter.objects.create(
        name=name,
        email=email,
        phone=phone,
        experience=experience,
        hourly_rate=hourly_rate
    )


def get_all_babysitters():
    return Babysitter.objects.all()


def get_babysitter(babysitter_id):
    return Babysitter.objects.get(id=babysitter_id)


def update_babysitter(
    babysitter_id,
    name,
    email,
    phone,
    experience,
    hourly_rate
):
    babysitter = Babysitter.objects.get(id=babysitter_id)

    babysitter.name = name
    babysitter.email = email
    babysitter.phone = phone
    babysitter.experience = experience
    babysitter.hourly_rate = hourly_rate

    babysitter.save()

    return babysitter


def delete_babysitter(babysitter_id):
    babysitter = Babysitter.objects.get(id=babysitter_id)
    babysitter.delete()