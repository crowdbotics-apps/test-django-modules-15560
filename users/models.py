from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


TYPE_VENDOR = 'vendor'
TYPE_CUSTOMER = 'customer'
USER_TYPES = (
    (TYPE_VENDOR, 'Vendor'),
    (TYPE_CUSTOMER, 'Customer'),
)


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, null=True, max_length=255)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    business_name = models.CharField(max_length=100, blank=True)
    user_type =  models.CharField(choices=USER_TYPES, max_length=20,
                    default=TYPE_CUSTOMER)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
