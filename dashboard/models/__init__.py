from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStampMixin(models.Model):
    """TimeStampMixin acts as parent class to models for adding creation and updation time fields

    Attributes
    ----------
    created_at : models.DateTimeField
        Auto adds the now value of datetime, and is not affected by further updates
    updated_at : models.DateTimeField
        Auto adds the now value of datetime, and is updated to new value when further updates happen
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MyUser(AbstractUser, TimeStampMixin):
    """MyUser model abstracted from django.contrib.auth.models.User

    Attributes
    ----------
    username
    password
    email
    is_staff
    is_superuser
    """

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
