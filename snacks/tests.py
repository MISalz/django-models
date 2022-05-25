from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model

def setUp(self):
        auditor = get_user_model().objects.create(username="tester",password="tester")
        Snack.objects.create(name="snack", purchaser=auditor, description="description")

# Create your tests here.

class SnacksTests(TestCase):
  def test_list_page_status_code(self):
    url = reverse("snack_list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)