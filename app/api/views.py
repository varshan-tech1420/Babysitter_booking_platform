from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from app.services.parent_service import get_all_parents
from app.services.babysitter_service import get_all_babysitters
from app.services.booking_service import create_booking


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists"
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("/login/")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")

        return render(request, "login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def parent_list(request):
    parents = get_all_parents()

    return render(request, "parents.html", {
        "parents": parents
    })


@login_required
def babysitter_list(request):
    babysitters = get_all_babysitters()

    return render(request, "babysitters.html", {
        "babysitters": babysitters
    })


@login_required
def booking_create(request):
    parents = get_all_parents()
    babysitters = get_all_babysitters()

    if request.method == "POST":
        parent_id = request.POST["parent_id"]
        babysitter_id = request.POST["babysitter_id"]
        booking_date = request.POST["booking_date"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]

        booking_date = datetime.strptime(
            booking_date, "%Y-%m-%d"
        ).date()

        start_time = datetime.strptime(
            start_time, "%H:%M"
        ).time()

        end_time = datetime.strptime(
            end_time, "%H:%M"
        ).time()

        create_booking(
            parent_id=parent_id,
            babysitter_id=babysitter_id,
            booking_date=booking_date,
            start_time=start_time,
            end_time=end_time
        )

        return redirect("/dashboard/")

    return render(request, "booking.html", {
        "parents": parents,
        "babysitters": babysitters
    })