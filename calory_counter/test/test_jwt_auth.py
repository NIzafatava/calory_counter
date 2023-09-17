from django.contrib.auth.models import User
from faker import Faker
from rest_framework.test import APITestCase
from rest_framework import status
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from django import test
from django.contrib.auth import get_user_model

User = get_user_model()

class TestJWTAuth(test.TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User(username="user", email="user@mail")
        user.set_password("password")
        user.save()

    def test_get_token(self):
        resp = self.client.post(
            "/api/token",
            {
                "username": "user",
                "password": "password"
            }
        )
        self.assertEqual(resp.status_code, 200)

        tokens = resp.json()
        print(tokens)

        self.assertTrue(tokens.get("access"))
        self.assertTrue(tokens.get("refresh"))

