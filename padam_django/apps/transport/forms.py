from django import forms
from .models import BusShift

class BusShiftForm(forms.ModelForm):

    class Meta:
        model = BusShift
        fields = ['bus', 'driver']
