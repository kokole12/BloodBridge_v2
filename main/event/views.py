from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView, 
    DetailView
)
# Create your views here.
def events(request):

    return HttpResponse("<h1> Events App </h1>")

class EventDetails(DeleteView):
    model = Event


class CreateEvent(LoginRequiredMixin,CreateView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date']

    def form_valid(self, form):
        form.instance.donor = self.request.user
        return super().form_valid(form)

class EventsList(ListView):
    model = Event
    context_object_name = 'event'
    ordering = ['-created_date']
    paginate_by = 3

class EventUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date']

    def form_valid(self, form):
        form.instance.donor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        appointment = self.get_object()
        if self.request.user == appointment.author:
            return True
        return False

class EventDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    """def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        """
