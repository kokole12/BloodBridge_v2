from django.urls import path
from .views import search_hopital, HospitalDetails


urlpatterns = [
    path('search_hospital/', view=search_hopital, name="search-hospital"),
    path('hospital_detail/<int:pk>/', view=HospitalDetails.as_view(), name="hospital-details")
    
]
