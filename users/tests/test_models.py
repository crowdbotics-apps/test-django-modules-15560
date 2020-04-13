import pytest

from django.test import TestCase
from django.conf import settings

from users.models import User


pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: settings.AUTH_USER_MODEL):
    assert user.get_absolute_url() == f"/users/{user.username}/"


class UserModelTests(TestCase):
    """Tests for users.User model."""

    def test_create_user_success(self):
        """Tests that create user successfully created."""
        first_name = 'First Name'
        last_name = 'Last Name'
        email = 'a@a.com'
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        self.assertEquals(user.first_name, first_name)

    def test_create_user_fail(self):
        """Tests that create user fails if there is no email."""
        first_name = 'First Name'
        last_name = 'Last Name'
        with self.assertRaises(ValueError):
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=None
            )
