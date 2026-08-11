from django.contrib import admin

from app.models.parent import Parent
from app.models.babysitter import Babysitter
from app.models.booking import Booking
from app.models.payment import Payment


admin.site.register(Parent)
admin.site.register(Babysitter)
admin.site.register(Booking)
admin.site.register(Payment)