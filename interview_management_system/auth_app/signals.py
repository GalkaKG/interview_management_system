from django.db.models.signals import post_save
from django.dispatch import receiver

from interview_management_system.auth_app.models import CustomUser, Profile


# from interview_management_system.auth_app.models import Interviewer, HR, CustomUser, Administrator


@receiver(post_save, sender=CustomUser)
def create_user_type(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



        # if instance.user_type == 'interviewer':
        #     Interviewer.objects.create(user=instance)
        # elif instance.user_type == 'hr':
        #     HR.objects.create(user=instance)
        # elif instance.user_type == 'admin':
        #     Administrator.objects.create(user=instance)



