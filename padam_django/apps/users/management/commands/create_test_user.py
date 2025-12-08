# padam_django/apps/users/management/commands/create_test_user.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.apps import apps

User = get_user_model()

class Command(BaseCommand):
    help = "Créer un compte test pour l'évaluateur avec mot de passe connu"

    def handle(self, *args, **kwargs):
        username = "andreechretien"
        password = "test12356"

        user, created = User.objects.get_or_create(username=username)
        user.set_password(password)
        user.is_staff = True  # pour avoir accès à l'admin
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Compte {username} créé avec succès."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Mot de passe pour {username} mis à jour."))
