# from django.shortcuts import render,redirect

# from django.contrib.auth.models import User

# from django.contrib.auth import authenticate

# from django.contrib.auth import login,logout

# from django.contrib.auth.decorators import login_required

# from .models import Profile,Ride

# def home(request):
#     return render(request,'home.html')

# def register(request):
#     if(request.method=="POST"):
#         user=User.objects.create_user(

#             username=request.POST['username'],
#             password=request.POST['password']
#         )

#         Profile.objects.create(

#             user=user,
#             role=request.POST['role']
#         )
#         return redirect('login')
#     return render(request,'register.html')

# def user_login(request):
#     if(request.method=="POST"):
#         user=authenticate(

#         username=request.POST['username'],
#         password=request.POST['password']
#         )

#         if(user):
#           login(request,login)
#           return redirect('home')
#     return render(request,"login.html")

# def user_logout(request):
#     logout(request)
#     return redirect('login')


# @login_required
# def book_ride(request):
#     if(request.method=="POST"):
#         Ride.objects.create(
#             customer=request.user,
#             pickup_location=request.POST["pickup_location"],
#             drop_location=request.POST["drop_location"],
#             fare=150

#         )

#         return redirect("my_rides")
#     return render(request,"book_ride.html")

# @login_required
# def my_rides(request):
#     ride=Ride.objects.filter(

#         customer=request.user
#     )
#     return render(request,"myrides.html",{'ride':ride})

# @login_required
# def available_rides(request):
#     rides=Ride.objects.filter(

#         status='REQUESTED'
#     )

#     return render(request,"available_rides.html",{'rides':rides})

# @login_required
# def accept_ride(request,ride_id):
#     ride=Ride.objects.get(id=ride_id)
#     ride=driver=request.user
#     ride.status='ACCEPTED'
#     ride.save()
#     return redirect('driver_rides')

# @login_required
# def driver_rides(request):
#     rides=Ride.objects.filter(
#         driver=request.user
#     )

#     return render(request,'driver_rides.html',{'rides':rides})

# @login_required
# def update_status(request,ride_id,status):
#     ride=Ride.objects.get(id=ride_id)
#     ride.status=status
#     ride.save()
#     return render(request,'driver_rides.html')






from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile, Ride


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if not username or not password or not role:
            messages.error(request, "All fields are required")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        Profile.objects.create(
            user=user,
            role=role
        )

        messages.success(request, "Registration successful")
        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def book_ride(request):
    if request.method == "POST":
        Ride.objects.create(
            customer=request.user,
            pickup_location=request.POST.get("pickup_location"),
            drop_location=request.POST.get("drop_location"),
            fare=150
        )

        messages.success(request, "Ride booked successfully")
        return redirect("my_rides")

    return render(request, "book_ride.html")


@login_required
def my_rides(request):
    rides = Ride.objects.filter(customer=request.user)

    return render(
        request,
        "myrides.html",
        {'ride': rides}
    )


@login_required
def available_rides(request):
    rides = Ride.objects.filter(status='REQUESTED')

    return render(
        request,
        "available_rides.html",
        {'rides': rides}
    )


@login_required
def accept_ride(request, ride_id):
    if request.method != "POST":
        return redirect('available_rides')

    profile = get_object_or_404(Profile, user=request.user)

    if profile.role != 'DRIVER':
        messages.error(request, "Only drivers can accept rides")
        return redirect('available_rides')

    ride = get_object_or_404(Ride, id=ride_id)

    if ride.status != 'REQUESTED':
        messages.error(request, "This ride is no longer available")
        return redirect('available_rides')

    ride.driver = request.user
    ride.status = 'ACCEPTED'
    ride.save()

    messages.success(request, "Ride accepted successfully")
    return redirect('driver_rides')


@login_required
def driver_rides(request):
    rides = Ride.objects.filter(driver=request.user)

    return render(
        request,
        'driver_rides.html',
        {'rides': rides}
    )


@login_required
def update_status(request, ride_id, status):
    if request.method != "POST":
        return redirect('driver_rides')

    profile = get_object_or_404(Profile, user=request.user)

    if profile.role != 'DRIVER':
        messages.error(request, "Only drivers can update ride status")
        return redirect('home')

    ride = get_object_or_404(
        Ride,
        id=ride_id,
        driver=request.user
    )

    allowed_statuses = ['ACCEPTED', 'COMPLETED', 'CANCELLED']

    if status not in allowed_statuses:
        messages.error(request, "Invalid ride status")
        return redirect('driver_rides')

    ride.status = status
    ride.save()

    messages.success(request, "Ride status updated successfully")
    return redirect('driver_rides')
