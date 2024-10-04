from . import views
from django.urls import path
from .views import (
    AppointmentListAPI, AppointmentDetailAPI,
    UserProfilesAPI, UserProfileDetailAPI,
    StylesAPI, StyleDetailAPI,
    ReviewsAPI, ReviewDetailAPI,
    StylesByStylistAPI  # Import the new view
)

urlpatterns = [
    path('appointments/', AppointmentListAPI.as_view(), name="AppointmentListAPI"),
    path('appointments/<int:pk>/', AppointmentDetailAPI.as_view(), name="AppointmentDetailAPI"),
    path('users/', UserProfilesAPI.as_view(), name="UserList"),
    path('users/<int:pk>/', UserProfileDetailAPI.as_view(), name="UserDetailAPI"),
    path('styles/', StylesAPI.as_view(), name="Styles"),
    path('', StylesAPI.as_view(), name="Styles"),
    path('styles/<int:pk>/', StyleDetailAPI.as_view(), name="StyleDetailAPI"),
    path('reviews/', ReviewsAPI.as_view(), name="ReviewsAPI"),
    path('reviews/<int:pk>/', ReviewDetailAPI.as_view(), name="ReviewDetailAPI"),
    path('styles/stylist/<int:stylist_id>/', StylesByStylistAPI.as_view(), name="StylesByStylistAPI"),  # New path for filtering styles
]
