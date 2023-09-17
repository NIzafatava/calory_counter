from django import test
from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from rest_framework import status
from ..models import Food, Exercise, Receipe

User = get_user_model()


class TestAPICreateFood(test.TestCase):
    @classmethod
    def setUpTestData(cls):
        Food.objects.create(
            name="food1",
            quantity=1,
            calorie=1000,
        )

        superuser_data = {"username": "super", "password": "password"}
        user_data = {"username": "user123", "password": "password"}

        User.objects.create_user(is_superuser=True, **superuser_data)
        User.objects.create_user(**user_data)

        cls.superuser_data = superuser_data
        cls.user_data = user_data

        cls.food_data = {
            'name':"food1",
            'quantity': 1,
            'calorie': 1000,
        }

    def setUp(self) -> None:
        self.superuser_tokens = self.client.post("/api/token", self.superuser_data).json()
        self.user_tokens = self.client.post("/api/token", self.user_data).json()

    def test_get_food_list(self):
        resp = self.client.get("/api/v1/foodlist/")

        food = Food.objects.get(name="food1")

        data = resp.json()
        print(data)
        self.assertTrue(data)

    def test_create_food_without_token(self):
        resp = self.client.post("/api/v1/foodlist/", self.food_data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
class TestAPICreateExercise(test.TestCase):
    @classmethod
    def setUpTestData(cls):
        Exercise.objects.create(
            name="exercise1",
            calorie=1000,
        )

        superuser__data = {"username": "super", "password": "password"}
        user_data = {"username": "user123", "password": "password"}

        User.objects.create_user(is_superuser=True, **superuser__data)
        User.objects.create_user(**user_data)

        cls.superuser_data = superuser__data
        cls.user_data = user_data

        cls.exercise_data = {
            'name':"recipe1",
            'calorie': 1000,
        }

    def setUp(self) -> None:
        self.superuser_tokens = self.client.post("/api/token", self.superuser_data).json()
        self.user_tokens = self.client.post("/api/token", self.user_data).json()

    def test_get_exercise_list(self):
        resp = self.client.get("/api/v1/exerciselist/")

        exercise = Exercise.objects.get(name="exercise1")

        data = resp.json()
        print(data)
        self.assertTrue(data)

    def test_create_exercise_without_token(self):
        resp = self.client.post("/api/v1/exerciselist/", self.exercise_data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)



class TestAPICreateRecipe(test.TestCase):
    @classmethod
    def setUpTestData(cls):
        Receipe.objects.create(
            name="recipe1",
            content='recip1',
        )

        superuser__data = {"username": "super", "password": "password"}
        user_data = {"username": "user123", "password": "password"}

        User.objects.create_user(is_superuser=True, **superuser__data)
        User.objects.create_user(**user_data)

        cls.superuser_data = superuser__data
        cls.user_data = user_data

        cls.recipe_data = {
            'name':"recipe1",
            'content': 'recip1',
        }

    def setUp(self) -> None:
        self.superuser_tokens = self.client.post("/api/token", self.superuser_data).json()
        self.user_tokens = self.client.post("/api/token", self.user_data).json()

    def test_get_recipe_list(self):
        resp = self.client.get("/api/v1/recipelist/")

        recipe = Receipe.objects.get(name="recipe1")

        data = resp.json()
        print(data)
        self.assertTrue(data)

    def test_create_recipe_without_token(self):
        resp = self.client.post("/api/v1/recipelist/", self.recipe_data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)