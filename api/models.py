from django.db import models
from django.utils import timezone


class EventBooking(models.Model):
    title = models.CharField(max_length=500, null=False)
    description = models.TextField(max_length=1500)
    location = models.CharField(max_length=400, null=True)
    event_date = models.DateTimeField(null=False, default=timezone.now)
    # start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    organizer = models.CharField(max_length=500, default="Unknown")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Title: {self.topic}, Date: {self.event_date}, Organizer: {self.organizer}"
        )


# class Event(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     topic = models.CharField(max_length=200, null=False)
#     description = models.TextField(null=True, blank=True)
#     event_date = models.DateTimeField(null=False, default=timezone.now)
#     location = models.TextField(max_length=400, null=True)
#     start_time = models.TimeField(null=True)
#     end_time = models.TimeField(null=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
