from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.reverse import reverse
from rest_framework import status
from api.base.models.model_auth import User


class RegisterTestCase(APITestCase):

    url = reverse("auth:register")

    def register_new_user_account(self):
        """
        Test to ensure it can register new user account
        """
        user_data = {
            "username": "username",
            "email": "user@user.com",
            "password": "password",
            "confirm_password": "password"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_password_validation(self):
        """
        Test to ensure confirm password equals to password
        """
        user_data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "password",
            "confirm_password": "passwordpass"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_unique_user_name(self):
        '''
        Test to ensure account can not be created with using same email
        '''

        user = User.objects.all()[:1]

        if user is not None:
            user_data = {
                "username": user[0].user_name,
                "email": "{}@{}.com".format(user[0].user_name, user[0].user_name),
                "password": "password",
                "confirm_password": "password"
            }
        response = self.client.post(self.url, user_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_unique_user_email(self):
        '''
        Test to ensure account can not be created with using same email
        '''
        user = User.objects.all()[:1]

        if user is not None:
            user_data = {
                "username": user.username + user.username,
                "email": user.email,
                "password": "password",
                "confirm_password": "password"
            }

        response = self.client.post(self.url, user_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
