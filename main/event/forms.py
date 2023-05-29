from django.forms import forms
from .models import Event
class StudentProfileForm(forms.ModelForm):

    event_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOE)', 'class': 'form-control'})
    )

    class Meta:
        model = Event
        fields = '__all__'