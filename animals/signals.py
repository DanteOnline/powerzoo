from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Food


@receiver(post_save, sender=Food)
def my_handler(sender, **kwargs):
    print('*'*100)
    print('SENDER', sender)
    print('kwargs', kwargs)
