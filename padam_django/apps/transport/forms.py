from django import forms
from django.core.exceptions import ValidationError
from .models import BusShift, BusStop

class BusShiftForm(forms.ModelForm):
    inline_formset = None  # sera injecté depuis l'admin

    class Meta:
        model = BusShift
        fields = ['bus', 'driver', 'status']

    def set_inline_formset(self, formset):
        """Injecte l'inline formset depuis l'admin."""
        self.inline_formset = formset

    def clean(self):
        cleaned_data = super().clean()

        if self.inline_formset:
            stops = [
                f.cleaned_data
                for f in self.inline_formset
                if not f.cleaned_data.get("DELETE")
            ]

            if len(stops) < 2:
                raise ValidationError("Un trajet doit avoir au moins 2 arrêts.")

        return cleaned_data
