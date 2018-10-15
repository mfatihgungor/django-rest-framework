from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email or not username:
            raise ValueError(
                'Users must have an email address and an username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given username,email
        and password.
        """
        if not email or not username:
            raise ValueError(
                'Users must have an email address and an username')

        user = self.create_user(
            username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):

    # CHOICES
    PREMIUM_TYPE_CHOICES = (
        ('WE', 'Weekly'),
        ('MO', 'Monthly'),
        ('AN', 'Annualy'),
    )

    # DATABASE FIELDS
    username = models.CharField(
        verbose_name='username',
        max_length=30,
        unique=True
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    premium_type = models.CharField(max_length=2, choices=PREMIUM_TYPE_CHOICES)
    is_premium = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # META CLASS
    class Meta:
        db_table = 'user_info'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # MANAGER
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def status_premium(self):
        return self.is_premium

    @status_premium.setter
    def status_premium(self, _status):
        if _status is not None:
            self.is_premium = _status

    @property
    def type_premium(self):
        return self.premium_type

    @type_premium.setter
    def type_premium(self, _type):
        if _type not in self.PREMIUM_TYPE_CHOICES:
            return None
        else:
            self.premium_type = _type
