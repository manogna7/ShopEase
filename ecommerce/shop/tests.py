from django.test import TestCase
from .models import Product, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(name="Laptop", category=self.category, price=1000.00, stock=50)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Laptop")

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Furniture")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Furniture")


class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='password')
        self.regular_user = User.objects.create_user(username='user', email='user@example.com', password='password')
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(name="Laptop", category=self.category, price=1000.00, stock=50)

    def test_admin_can_create_product(self):
        self.client.login(username='admin', password='password')
        response = self.client.post('/api/products/', {'name': 'Tablet', 'category': self.category.id, 'price': 500.00, 'stock': 30})
        self.assertEqual(response.status_code, 201)

    def test_regular_user_cannot_create_product(self):
        self.client.login(username='user', password='password')
        response = self.client.post('/api/products/', {'name': 'Tablet', 'category': self.category.id, 'price': 500.00, 'stock': 30})
        self.assertEqual(response.status_code, 403)