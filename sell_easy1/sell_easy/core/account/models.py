from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from uuid import uuid4

# Create your models here.
class ProfileManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if email is None:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        if email is None:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)

        extra_fields['is_admin'] = True
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_seller'] = True

        user = self.create_user(email=email, password=password, **extra_fields)
        return user

    # def create_seller(self, email, password, **extra_fields):

    #     if email is None:
    #         raise ValueError('Email is required')
        
    #     email = self.normalize_email(email)
    #     extra_fields.is_seller = True

    #     seller = self.create_user(email=email, password=password, **extra_fields)

    #     store = Store(owner = seller, name=extra_fields.name, tagline = extra_fields.tagline)
        
    #     return seller, store

class Profile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    is_verified = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    #Model.objects.create_user
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ('first_name', 'last_name', 'password')

    objects = ProfileManager()
 
    def __str__(self) -> str:
        return self.get_full_name()


