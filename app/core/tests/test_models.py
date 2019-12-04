from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_success(self):
        """test creating a new users with an email is successful"""
        email = "firstuser@test.com"
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email of the new user is normalized"""
        email = "amine@YAHOO.fr"
        user = get_user_model().objects.create_user(email, "pass123456")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if email is empty then raise an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test created new super user"""
        superuser = get_user_model().objects.create_superuser("amine@yahoo.fr", "test123")
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)