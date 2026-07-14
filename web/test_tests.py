from django.test import TestCase
from django.urls import reverse

class TestTestView(TestCase):
     def test_test_view(self):
         url = reverse('test')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "This is a test vie.")