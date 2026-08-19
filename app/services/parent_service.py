from app.models.parent import Parent


def create_parent(name, email, phone, address):
    return Parent.objects.create(
        name=name,
        email=email,
        phone=phone,
        address=address
    )


def get_all_parents():
    return Parent.objects.all()


def get_parent(parent_id):
    return Parent.objects.get(id=parent_id)


def update_parent(parent_id, name, email, phone, address):
    parent = Parent.objects.get(id=parent_id)

    parent.name = name
    parent.email = email
    parent.phone = phone
    parent.address = address

    parent.save()

    return parent


def delete_parent(parent_id):
    parent = Parent.objects.get(id=parent_id)
    parent.delete()