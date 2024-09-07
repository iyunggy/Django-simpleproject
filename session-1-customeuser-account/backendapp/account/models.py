from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
import datetime

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, first_name, is_staff, is_active, password,
    **extra_fields):

        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(  
          email=email,
          first_name=first_name,
          is_staff=is_staff,
          is_active=is_active,
          **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self,  email, first_name,  is_staff, is_active,password=None, **extra_fields):
        return self._create_user(email, first_name, is_staff, True, password, **extra_fields)

    def create_superuser(self, email, first_name, is_staff, is_active, password=None, **extra_fields):
        return self._create_user(email, first_name,  True, True, password,  **extra_fields)


class User(AbstractUser, PermissionsMixin):
  created_at = models.DateTimeField(default=datetime.datetime.now)
  email = models.EmailField(max_length=255, unique=True)
  first_name = models.CharField(max_length=255, default='')
  last_name = models.CharField(max_length=255, default='')
  phone = models.CharField(max_length=255, default='')
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'is_active', 'is_staff']

  objects = UserManager()

  # def save(self, *args, **kwargs):
  #   self.email = self.email.lower()
  #   return super().save(*args, **kwargs)
  
  # def __str__(self) -> str:
  #   return '{}'.format(self.email)
