from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create user groups'

    def handle(self, *args, **options):
        administrator_group, _ = Group.objects.get_or_create(name='Administrators')
        hr_group, _ = Group.objects.get_or_create(name='HR')
        interviewer_group, _ = Group.objects.get_or_create(name='Interviewers')

        self.stdout.write(self.style.SUCCESS('User groups created successfully.'))
