from django import forms
from .models import BusShift

class BusShiftForm(forms.ModelForm):
    inline_formset = None

    class Meta:
        model = BusShift
        fields = ['bus', 'driver', 'status']
