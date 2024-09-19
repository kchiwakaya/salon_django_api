from django.contrib import admin
from .models import  UserProfile,Style, Appointment, Image, Review


admin.site.register(Style)
admin.site.register(Appointment)
admin.site.register(UserProfile)
admin.site.register(Image)
admin.site.register(Review)


