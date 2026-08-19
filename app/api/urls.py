from django.urls import path

from app.api.views import (
    home,
    register,
    login_view,
    logout_view,
    dashboard,
    parent_list,
    babysitter_list,
    booking_create,
)


urlpatterns = [
    path("", home, name="home"),

    path("register/", register, name="register"),

    path("login/", login_view, name="login"),

    path("logout/", logout_view, name="logout"),

    path("dashboard/", dashboard, name="dashboard"),

    path("parents/", parent_list, name="parent_list"),

    path("babysitters/", babysitter_list, name="babysitter_list"),

    path("booking/", booking_create, name="booking_create"),
]