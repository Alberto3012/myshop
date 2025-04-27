from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Rol(models.Model):
    rol_name = models.CharField(max_length=20)
    is_admin = models.BooleanField(blank=False, null=False)

    class Meta:
        db_table = 'rol' 

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, default=1)
    last_login = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group', related_name='user_groups', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='user_permissions', blank=True
    )

    class Meta:
        db_table = 'users'


