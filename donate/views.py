from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Appointment
# Create your views here.
def home(request):
    return render(request, 'donate/home.html')

class AppointmentDetail(DetailView):
    model = Appointment


class CreateAppointment(LoginRequiredMixin, CreateView):
    model = Appointment
    fields = ['reason', 'contact']

    def form_valid(self, form):
        form.instance.donor = self.request.user
        return super().form_valid(form)

class UpdateAppointment(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Appointment
    fields = ['reason', 'contact']

    def form_valid(self, form):
        form.instance.donor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        appointment = self.get_object()
        if self.request.user == appointment.donor:
            return True
        return False

class DeleteAppoinment(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Appointment
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.donor:
            return True
        return False
