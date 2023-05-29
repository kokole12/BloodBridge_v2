from django.urls import path
from .views import home, CreateAppointment, AppointmentDetail, UpdateAppointment, DeleteAppoinment

urlpatterns = [
    path('', view=home, name="home"),
    path('appointment/<int:pk>/', view=AppointmentDetail.as_view(), name='appointment-detail'),
    path('appointment/new/', view=CreateAppointment.as_view(), name='appointment'),
    path('appointment/<int:pk>/update/',view=UpdateAppointment.as_view(), name="appointment-update"),
    path('appointment/<int:pk>/delete/',view=DeleteAppoinment.as_view(), name="delete-appointment"),
]
