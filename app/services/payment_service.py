from app.models.payment import Payment
from app.models.booking import Booking


def create_payment(booking_id, amount):
    booking = Booking.objects.get(id=booking_id)

    return Payment.objects.create(
        booking=booking,
        amount=amount
    )


def get_all_payments():
    return Payment.objects.all()


def get_payment(payment_id):
    return Payment.objects.get(id=payment_id)


def update_payment(payment_id, amount, payment_status):
    payment = Payment.objects.get(id=payment_id)

    payment.amount = amount
    payment.payment_status = payment_status

    payment.save()

    return payment


def update_payment_status(payment_id, payment_status):
    payment = Payment.objects.get(id=payment_id)

    payment.payment_status = payment_status
    payment.save()

    return payment


def delete_payment(payment_id):
    payment = Payment.objects.get(id=payment_id)
    payment.delete()