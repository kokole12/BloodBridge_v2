from django.urls import path
from .views import events, CreateEvent, EventDetails, EventsList, EventUpdate, EventDelete


urlpatterns = [
    path('event/', view=events, name='events'),
    path("events/", EventsList.as_view(), name="events-list"),
    path("event/<int:pk>/update/", EventUpdate.as_view(), name="event-update"),
    path('event/<int:pk>/delete/', view=EventDelete.as_view(), name='event-delete'),
    path('event/new/',view=CreateEvent.as_view(), name="event-create"),
    path('event/<int:pk>/', view=EventDetails.as_view(), name="event-detail"),
]
