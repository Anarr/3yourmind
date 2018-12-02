from django.test import TestCase
from django.test import Client
from django.urls import reverse
import json
# Create your tests here.


class CatApiIndexViews(TestCase):
    def test_get_cats(self):
        """
        test cats list api
        """
        response = self.client.get('/api/cats/kittens/', {'limit': 3})
        content = json.loads(response.content)

        self.assertEqual(content['code'], 200)
        self.assertEqual(len(content['data']), 3)
        self.assertEqual(response.status_code, 200)

    def test_get_categories(self):
        """
        test categories list api.
        """
        response = self.client.get(reverse('categories'))
        content = json.loads(response.content)

        self.assertEqual(content['code'], 200)
        self.assertEqual(response.status_code, 200)