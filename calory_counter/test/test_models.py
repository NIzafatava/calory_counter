from django.contrib.auth import get_user_model
from django.test import TestCase

from calory_counter.models import Food

User = get_user_model()


class FoodModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Food.objects.create(name="food1", quantity=10, calorie=100)

    def test_name_food_label(self):
        food = Food.objects.get(id=1)

        field_verboses = {
            "name": "name",
            "quantity": "quantity",
            "calorie": "calorie",
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    food._meta.get_field(field).verbose_name, expected_value
                )

    def test_max_lenght_label_name(self):
        food = Food.objects.get(id=1)
        max_lenght = food._meta.get_field("name").max_length
        self.assertEquals(max_lenght, 200)
