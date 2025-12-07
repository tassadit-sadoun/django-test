from django.contrib import admin

from .bus_shift_service import update_shift_times
from .forms import BusShiftForm
from .models import BusShift, BusStop


class BusStopInline(admin.TabularInline):
    model = BusStop
    extra = 2
    fields = ('place', 'time', 'order')
    ordering = ('order',)

@admin.register(BusShift)
class BusShiftAdmin(admin.ModelAdmin):
    form = BusShiftForm
    inlines = [BusStopInline]
    list_display = ['bus', 'driver', 'status', 'start_time', 'end_time', 'duration']
    search_fields = ['bus__licence_plate', 'driver__user__username']

    def save_formset(self, request, form, formset, change):
        """
        Sauvegarde des inlines puis calcul automatique des temps du trajet.
        """
        super().save_formset(request, form, formset, change)
        # Calcul des temps et vérification chevauchements
        update_shift_times(form.instance)
