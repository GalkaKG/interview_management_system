from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from interview_management_system.auth_app.models import CustomUser


class Command(BaseCommand):
    help = 'Create custom permissions and assign them to groups'

    def handle(self, *args, **kwargs):
        can_view_candidate = Permission.objects.create(
            codename='can_view_candidate',
            name='Can view candidate details'
        )
        can_schedule_interview = Permission.objects.create(
            codename='can_schedule_interview',
            name='Can schedule interviews'
        )

        user_types = [choice[0] for choice in CustomUser.USER_TYPES]

        for user_type in user_types:
            group = Group.objects.get(name=user_type)
            group.permissions.add(can_view_candidate)
            if user_type in ['hr', 'admin']:
                group.permissions.add(can_schedule_interview)
                group.permissions.add(can_view_candidate)

        self.stdout.write(self.style.SUCCESS('Custom permissions created and assigned.'))



# Run python manage.py create_permissions
