from django.contrib.auth import get_user_model
from django.test import TestCase
from user.models import Profile, PostFood
from calory_counter.models import Food
User = get_user_model()
class FoodModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Food.objects.create(name='food1', quantity=10,calorie=100)

    def test_name_food_label(self):
        food = Food.objects.get(id=1)

        field_verboses = {
            'name': 'name',
            'quantity': 'quantity',
            'calorie': 'calorie',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    food._meta.get_field(field).verbose_name, expected_value)
    def test_max_lenght_label_name(self):
        food = Food.objects.get(id=1)
        max_lenght = food._meta.get_field('name').max_length
        self.assertEquals(max_lenght, 200)


# class ProfileModelTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         super().setUpClass()
#
#         superuser_data = {"username": "super", "password": "password"}
#         user_data = {"username": "user123", "password": "password"}
#
#         User.objects.create_user(is_superuser=True, **superuser_data)
#         user1 = User.objects.create_user(**user_data)
#         cls.profile = Profile.objects.create(person_of=user1, food_selected='Avocado', calorie_count=100, quantity=10,
#                                              meat_type='lunch')

    # def test_create_item_in_post(self):
    #     post= PostFood.objects.get(profile=1)
    #     person_id = post.profile
    #     self.assertEquals(person_id, 1)

