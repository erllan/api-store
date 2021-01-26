from .models import Order, User, Category, Product, Curt
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestApi(APITestCase):
    def test_create_category(self):
        data = {
            "name": "test"
        }
        response = self.client.post('/api/category/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_get_category(self):
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
