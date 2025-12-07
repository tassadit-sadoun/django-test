from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.apps import apps

User = get_user_model()

class Command(BaseCommand):
    help = "Met à jour tous les utilisateurs non-driver pour qu'ils puissent accéder aux BusShift dans l'admin"

    def handle(self, *args, **options):

        # Récupérer les permissions add/change/view
        busshift_perms = Permission.objects.filter(
            content_type__app_label='transport',
            content_type__model='busshift',
            codename__in=['add_busshift', 'change_busshift', 'view_busshift']
        )

        
        # Permissions BusStop
        busstop_perms = Permission.objects.filter(
            content_type__app_label='transport',
            content_type__model='busstop',
            codename__in=['add_busstop', 'change_busstop', 'view_busstop']
        )

        # Filtrer les utilisateurs non drivers
        non_drivers = User.objects.filter(driver__isnull=True)
        count = 0

        for user in non_drivers:
            user.is_staff = True
            user.user_permissions.add(*busshift_perms)
            user.user_permissions.add(*busstop_perms)
            user.save()
            count += 1

        self.stdout.write(self.style.SUCCESS(
            f"{count} utilisateurs non-driver mis à jour avec is_staff=True et permissions BusShift."
        ))
