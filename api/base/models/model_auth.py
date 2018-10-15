from django.db import models
from django.conf import settings

class User(models.Model):

    # CHOICES
    PREMIUM_TYPE_CHOICES = (
        ('WE', 'Weekly'),
        ('MO', 'Monthly'),
        ('AN', 'Annualy'),
    )

    # DATABASE FIELDS
    # unique auto increment key
    user_id = models.AutoField('id', primary_key=True)
    user_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    last_login_date = models.DateTimeField()
    client_id = models.CharField(max_length=100)
    is_premium = models.BooleanField()
    premium_type = models.CharField(max_length=2, choices=PREMIUM_TYPE_CHOICES)
    is_active = models.BooleanField()

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        db_table = 'user_info'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # MODEL METHODS
    def __str__(self):
        return self.user_id

    def save(self, *args, **kwargs):
        if settings.DEBUG:
            # TODO make a print call
            super().save(*args, **kwargs)  # Call the "real" save() method.
            # TODO make a print call

        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)  # Call the "real" delete() method.

    # OTHER METHODS

    def premium_status(self):
        """ Returns the user's premium status. """
        if self.is_premium:
            return self.premium_type
        else:
            return self.is_premium

    @property
    def full_name(self):
        """ Returns user's full name. """
        return '%s %s' % (self.first_name, self.last_name)
