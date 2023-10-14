from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from interview_management_system.interview_management.models import Interview


# Function to create groups and assign permissions
def create_groups_and_permissions():
    # Create groups for each role
    interviewer_group, created = Group.objects.get_or_create(name='Interviewer')
    hr_group, created = Group.objects.get_or_create(name='HR')
    admin_group, created = Group.objects.get_or_create(name='Administrator')

    # Define permissions
    content_type = ContentType.objects.get_for_model(Interview)
    permission_create_interview = Permission.objects.get(codename='create_interview')
    permission_view_interview = Permission.objects.get(codename='view_interview')
    permission_delete_interview = Permission.objects.get(codename='delete_interview')

    # permission1 = Permission.objects.get(codename='can_do_something1')
    # permission2 = Permission.objects.get(codename='can_do_something2')
    # permission3 = Permission.objects.get(codename='can_do_something3')
    # Add more permissions as needed

    interviewer_group.permissions.add(permission_create_interview, permission_view_interview)
    hr_group.permissions.add(permission_view_interview, permission_delete_interview)
    admin_group.permissions.add(permission_create_interview, permission_delete_interview)


if __name__ == '__main__':
    create_groups_and_permissions()
