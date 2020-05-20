from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    # test creating a new user with email an address is successful
    def test_create_user_with_email_successful(self):
        email = "tanveer@gmail.com"
        password = 'meer123!'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """normalizing user email"""
        email = "tanver@GMAIL.COM"

        user = get_user_model().objects.create_user(email, '1234567890')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email_error(self):
        """checking if email is provided or not and raising a value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12345678')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'tanveer@gmail.com',
            '1234!'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
