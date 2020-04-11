from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'test@szczecin.pl'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for new user is normalized"""
        email = 'test@SZCZECIN.PL'
        user = get_user_model().objects.create_user(email, 'test')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')

    def test_create_new_super_user(self):
        """Test createing new super user"""
        user = get_user_model().objects.create_superuser(
            'test@szczecin.com',
            'test',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
