from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.username


