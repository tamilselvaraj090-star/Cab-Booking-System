from django.contrib import admin
# from django.urls import path
# from .views import home,register,user_login,user_logout,book_ride,my_rides,available_rides,accept_ride,driver_rides,update_status

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',home,name='home'),
#     path('register/',register,name='register'),
#     path('login/',user_login,name='login'),
#     path('logout/',user_logout,name='logout'),
#     path('book/',book_ride,name='book_ride'),
#     path('myrides/',my_rides,name='my_rides'),
#     path('available_rides/',available_rides,name='available_rides'),
#     path('accept/<int:ride_id>/',accept_ride,name='accept'),
#     path('driver_rides/',driver_rides,name='driver_rides'),
#     path('status/<int:ride_id>/<str:status>/',update_status,name='update_status'),

# ]




from django.urls import path
from .views import (
    home,
    register,
    user_login,
    user_logout,
    book_ride,
    my_rides,
    available_rides,
    accept_ride,
    driver_rides,
    update_status,
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('book/', book_ride, name='book_ride'),
    path('myrides/', my_rides, name='my_rides'),
    path('available_rides/', available_rides, name='available_rides'),
    path('accept/<int:ride_id>/', accept_ride, name='accept'),
    path('driver_rides/', driver_rides, name='driver_rides'),
    path('status/<int:ride_id>/<str:status>/', update_status, name='update_status'),
]
