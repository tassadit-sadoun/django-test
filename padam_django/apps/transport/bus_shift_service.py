from django.db import transaction
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import BusShift

def update_shift_times(shift):
    """
    Met à jour start_time, end_time et duration pour un BusShift
    après la sauvegarde des BusStop.
    """
    stops = list(shift.stops.all())
    with transaction.atomic():
        # Lock du shift pour éviter modifications concurrentes
        shift = BusShift.objects.select_for_update().get(pk=shift.pk)
        if len(stops) < 2:
            raise ValidationError("Un trajet doit avoir au moins 2 arrêts.")

        # Tri par order
        stops_sorted = sorted(stops, key=lambda s: s.order)
        shift.start_time = stops_sorted[0].time
        shift.end_time = stops_sorted[-1].time
        shift.duration = shift.end_time - shift.start_time

        # Validation cohérente
        if shift.end_time <= shift.start_time:
            raise ValidationError("La fin doit être après le début.")

        # Vérification chevauchements bus/driver
        overlapping = shift.__class__.objects.exclude(pk=shift.pk).filter(
            Q(bus=shift.bus) | Q(driver=shift.driver),
            start_time__lt=shift.end_time,
            end_time__gt=shift.start_time,
        )
        if overlapping.exists():
            raise ValidationError("Ce trajet chevauche un autre trajet existant.")

        shift.save()
