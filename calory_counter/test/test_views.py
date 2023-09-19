from django.test import TestCase, Client
from django.urls import reverse

from calory_counter.models import Receipe


class RecipesViewTestGet(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_recipe_url = reverse("calory_counter:receipes")
        self.detail_recipe_url = reverse("calory_counter:show", args="1")
        Receipe.objects.create(id=1, name="recipe1")

    def test_recipes_all_get(self):
        response = self.client.get(self.list_recipe_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "receipe_page.html")

    def test_detail_recipe_get(self):
        response = self.client.get(self.detail_recipe_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "recipe_details.html")
