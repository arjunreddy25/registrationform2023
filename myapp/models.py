from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser,Permission

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )




