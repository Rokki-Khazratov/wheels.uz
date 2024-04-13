from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Detail

@receiver(post_save, sender=Detail)
def add_detail_to_wheel(sender, instance, **kwargs):
    if instance.wheel:
        instance.wheel.details.add(instance)