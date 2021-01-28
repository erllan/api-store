from .models import Order, User, Category, Product
from rest_framework.test import APITestCase,APIClient,RequestsClient
from rest_framework import status
import json
from django.test import Client


class TestApi(APITestCase):
    def setUp(self):
        self.requests = RequestsClient()
        user = User.objects.create(username="test1", email="test1@mail.com")
        user.set_password("xxxxcikadada21321")
        user.is_active = True
        user.save()
        Product.objects.create(title="test", price=12)

    def test_register(self):
        data = {
            "username": "test",
            "email": "test@mail.com",
            "password": "xxxxcikada112233"

        }
        response = self.client.post("/api/user/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def user_get_token(self):
        data = {
            "username": "test1",
            "password": "xxxxcikadada21321"
        }
        response = self.client.post("/api/user/token/", data)
        return response.data['access']

    def test_create_category(self):
        token = self.user_get_token()
        data = {
            "name": "test"
        }
        response = self.client.post('/api/category/', data, HTTP_AUTHORIZATION='Bearer {}'.format(token))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_get_category(self):
        token = self.user_get_token()
        response = self.client.get('/api/category/', HTTP_AUTHORIZATION='Bearer {}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        token = self.user_get_token()
        data = {
            "title": "test_product",
            "price": 2,
            "category": 1
        }

        request = self.client.post('/api/product/', data, HTTP_AUTHORIZATION='Bearer {}'.format(token))
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_product(self):
        token = self.user_get_token()
        request = self.client.get('/api/product/', HTTP_AUTHORIZATION='Bearer {}'.format(token))

        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_curt(self):
        user = {
            "username": "test1",
            "password": "xxxxcikadada21321"
        }
        self.client.login(**user)
        request = self.client.get('/api/curt/')
        self.assertEqual(request.status_code,200)

    def test_order(self):
        user = {
            "username": "test1",
            "password": "xxxxcikadada21321"
        }
        data = {
            "total": 2,
            "product": 1
        }
        request = self.client.post('/api/order/', data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED,)
