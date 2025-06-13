import random

from Tools.demo.mcast import sender
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from cake_app.models import Baker, Cake


@receiver(pre_delete, sender=Baker)
def assign_cakes_after_baker_deletion(sender, instance, **kwargs):
    cakes=Cake.objects.filter(baker=instance).all()

    other_bakers=Baker.objects.exclude(id=instance.id).all()

    for cake in cakes:
        new_baker=random.choice(other_bakers)
        cake.baker=new_baker
        cake.save()

