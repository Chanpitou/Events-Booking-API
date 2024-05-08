from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EventBooking
from .serializers import EventBookingSerializer


# Show the available routes for the api
@api_view(["GET"])
def getRoutes(request):
    routes = [
        "To get all events:       /eventbooking-search/",
        "To get specified events: /eventbooking-search/?title=title_name",
        "To create events:        /eventbooking-create/",
        "To update events:        /eventbooking-update/<id>/",
        "To delete events:        /eventbooking-delete/<id>/",
    ]
    return Response(routes)


# get event
class EventBookingSearch(APIView):
    def get(self, request, format=None):
        # example: /eventbooking-search/?title=career
        title = request.query_params.get("title", "")

        if title:
            events = EventBooking.objects.filter(title__icontains=title)
        else:
            events = EventBooking.objects.all()

        serializer = EventBookingSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# creating event
class EventBookingCreate(generics.CreateAPIView):
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer


# update event
class EventBookingUpdate(generics.RetrieveUpdateAPIView):
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer
    lookup_field = "pk"


# delete event
class EventBookingDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer
    lookup_field = "pk"
