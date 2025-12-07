from django.db import models

class BusShift(models.Model):
    bus = models.ForeignKey('fleet.Bus', on_delete=models.PROTECT, related_name='shifts')
    driver = models.ForeignKey('fleet.Driver', on_delete=models.PROTECT, related_name='shifts')
    status = models.CharField(max_length=20, default='Brouillon')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

class BusStop(models.Model):
    shift = models.ForeignKey(BusShift, on_delete=models.CASCADE, related_name='stops')
    place = models.ForeignKey('geography.Place', on_delete=models.PROTECT)
    time = models.DateTimeField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(fields=['shift', 'order'], name='unique_stop_order_per_shift')
        ]
