from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

from padam_django.apps.transport.models import BusShift, BusStop
from padam_django.apps.fleet.models import Bus, Driver
from padam_django.apps.geography.models import Place
from padam_django.apps.users.models import User
from django.utils import timezone

from ..bus_shift_service import update_shift_times


class UpdateShiftTimesTest(TestCase):

    def setUp(self):
        # Création d’un User obligatoire pour Driver
        self.user = User.objects.create(username="driver1")

        # Driver valide
        self.driver = Driver.objects.create(user=self.user)

        # Bus valide
        self.bus = Bus.objects.create(licence_plate="ABC123")

        # Places valides (avec coordonnées obligatoires)
        self.placeA = Place.objects.create(name="A", latitude=48.8566, longitude=2.3522)
        self.placeB = Place.objects.create(name="B", latitude=48.8570, longitude=2.3530)
        self.placeC = Place.objects.create(name="C", latitude=48.8575, longitude=2.3540)
        self.placeD = Place.objects.create(name="D", latitude=48.8580, longitude=2.3550)

    def test_less_than_two_stops_raises_error(self):
        shift = BusShift.objects.create(bus=self.bus, driver=self.driver)

        BusStop.objects.create(
            shift=shift,
            place=self.placeA,
            time=datetime.now(),
            order=1
        )

        with self.assertRaises(ValidationError):
            update_shift_times(shift)

    def test_correct_start_end_duration(self):
        shift = BusShift.objects.create(bus=self.bus, driver=self.driver)
        now = timezone.now()

        stop1 = BusStop.objects.create(
            shift=shift,
            place=self.placeA,
            time=now,
            order=2
        )

        stop2 = BusStop.objects.create(
            shift=shift,
            place=self.placeB,
            time=now + timedelta(minutes=30),
            order=1
        )

        update_shift_times(shift)
        shift.refresh_from_db()

        self.assertEqual(shift.start_time, stop2.time)
        self.assertEqual(shift.end_time, stop1.time)
        self.assertEqual(shift.duration, stop1.time - stop2.time)

    def test_overlapping_shift_raises_error(self):
        now = datetime.now()

        shift1 = BusShift.objects.create(bus=self.bus, driver=self.driver)
        BusStop.objects.create(shift=shift1, place=self.placeA, time=now, order=1)
        BusStop.objects.create(shift=shift1, place=self.placeB, time=now + timedelta(minutes=30), order=2)

        shift2 = BusShift.objects.create(bus=self.bus, driver=self.driver)
        BusStop.objects.create(shift=shift2, place=self.placeC, time=now + timedelta(minutes=15), order=1)
        BusStop.objects.create(shift=shift2, place=self.placeD, time=now + timedelta(minutes=45), order=2)

        # shift1 est valide
        update_shift_times(shift1)

        # shift2 chevauche → doit lever une erreur
        with self.assertRaises(ValidationError):
            update_shift_times(shift2)
