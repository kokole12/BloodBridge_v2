from django.shortcuts import render, HttpResponse
from .models import Hospital
from django.views.generic import DetailView

# Create your views here.
def search_hopital(request):
    if request.method == "POST":
        search = request.POST['search']
        hospital = Hospital.objects.filter(name__contains=search)
        return render(request, 'hospital/search_hospital.html', {"search": search, "hospital": hospital})
    else:
        None


class HospitalDetails(DetailView):
    model = Hospital
