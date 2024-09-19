from django.contrib import admin
from .models import  UserProfile,Style, Appointment,  Review


admin.site.register(Style)
admin.site.register(Appointment)
admin.site.register(UserProfile)
admin.site.register(Review)


