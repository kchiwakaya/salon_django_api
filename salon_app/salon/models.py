from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    types = (
       ('clt','Customer'),
       ('hd','Hairdresser'),
       ('bb','Barber'),
       ('stl','Nail Stylist')
    )
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length = 255,blank=True)
    phone_number = models.CharField(max_length = 20,blank = True)
    salon_name = models.CharField(max_length = 50,blank = True)
    mirror_number = models.CharField(max_length  = 50,blank=True)
    user_type = models.CharField(max_length= 20,choices = types)
    city = models.CharField(max_length= 20)
    profile_pic_url = models.URLField(max_length=255, blank=True)
    

class Style(models.Model):
    stylist = models.ForeignKey(UserProfile, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    images = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    client = models.ForeignKey(UserProfile, related_name='appointments', on_delete=models.CASCADE)
    stylist = models.ForeignKey(UserProfile, related_name='booked_appointments', on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    stylist = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='stylist_reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment
    

