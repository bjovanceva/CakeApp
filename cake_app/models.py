from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Baker(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    surname = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    photo = models.ImageField(upload_to='backers/', null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Cake(models.Model):
    name=models.CharField(max_length=250, null=True, blank=True)
    price=models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    weight=models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    photo=models.ImageField(upload_to='cakes/', null=True, blank=True)
    baker=models.ForeignKey(Baker, on_delete=models.CASCADE, null=True, blank=True, related_name='cakes')

    def __str__(self):
        # return f"{self.name}"
        return self.name



