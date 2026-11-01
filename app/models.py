# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     ROLE_CHOICES=(

#         ('CUSTOMER','Customer'),
#         ('DRIVER','Driver'),
#     )
#     user=models.OneToOneField (User,on_delete=models.CASCADE)
#     role=models.CharField(max_length=20,choices=ROLE_CHOICES)

# class Ride(models.Model):  
#     STATUS_CHOICES=(

#         ('REQUESTED','Requested'),
#         ('ACCEPTED','Accepted'),
#         ('STARTED','Started'),
#         ('COMPLETED','Completed'),
#         ('CANCELLED','Cancelled'),
#     )

#     customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer_rides')
#     drive=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='driver_rides')
#     pickup_location=models.CharField(max_length=200)
#     drop_location=models.CharField(max_length=200)
#     fare=models.IntegerField(default=150)
#     status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='REQUESTED')
#     create_at=models.DateTimeField(auto_now_add=True)






    
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    ROLE_CHOICES = (
        ('CUSTOMER', 'Customer'),
        ('DRIVER', 'Driver'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Ride(models.Model):

    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('ACCEPTED', 'Accepted'),
        ('STARTED', 'Started'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='customer_rides'
    )

    driver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='driver_rides'
    )

    pickup_location = models.CharField(max_length=200)

    drop_location = models.CharField(max_length=200)

    fare = models.IntegerField(default=150)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='REQUESTED'
    )

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"


