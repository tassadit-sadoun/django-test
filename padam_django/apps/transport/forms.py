from django import forms
from django.core.exceptions import ValidationError
from .models import BusShift

class BusShiftForm(forms.ModelForm):
    inline_formset = None  # sera injecté depuis l'admin

    class Meta:
        model = BusShift
        fields = ['bus', 'driver', 'status']

    def set_inline_formset(self, formset):
        """Injecte l'inline formset depuis l'admin."""
        self.inline_formset = formset

    def clean(self):
        return super().clean()

