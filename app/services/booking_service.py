from app.models.booking import Booking
from app.models.parent import Parent
from app.models.babysitter import Babysitter


def create_booking(
    parent_id,
    babysitter_id,
    booking_date,
    start_time,
    end_time
):
    parent = Parent.objects.get(id=parent_id)
    babysitter = Babysitter.objects.get(id=babysitter_id)

    return Booking.objects.create(
        parent=parent,
        babysitter=babysitter,
        booking_date=booking_date,
        start_time=start_time,
        end_time=end_time,
        status="pending"
    )


def get_all_bookings():
    return Booking.objects.all()


def get_booking(booking_id):
    return Booking.objects.get(id=booking_id)


def update_booking(
    booking_id,
    booking_date,
    start_time,
    end_time,
    status
):
    booking = Booking.objects.get(id=booking_id)

    booking.booking_date = booking_date
    booking.start_time = start_time
    booking.end_time = end_time
    booking.status = status

    booking.save()

    return booking


def delete_booking(booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()


def update_booking_status(booking_id, status):
    booking = Booking.objects.get(id=booking_id)

    booking.status = status
    booking.save()

    return booking