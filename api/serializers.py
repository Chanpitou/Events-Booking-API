from rest_framework import serializers
from .models import EventBooking


class EventBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = [
            "title",
            "description",
            "location",
            "event_date",
            "end_time",
            "organizer",
        ]
