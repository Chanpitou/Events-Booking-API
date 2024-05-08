from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path(
        "eventbooking-search/",
        views.EventBookingSearch.as_view(),
        name="event-booking-search",
    ),
    path(
        "eventbooking-create/",
        views.EventBookingCreate.as_view(),
        name="event-booking-create",
    ),
    path(
        "eventbooking-update/<int:pk>/",
        views.EventBookingUpdate.as_view(),
        name="event-booking-update",
    ),
    path(
        "eventbooking-delete/<int:pk>/",
        views.EventBookingDelete.as_view(),
        name="event-booking-delete",
    ),
]
