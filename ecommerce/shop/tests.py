from django.test import TestCase
from .models import Product, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status, generics
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer

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


class CategoryTests(APITestCase):

    def test_create_category(self):
        url = reverse('category-list-create')
        data = {'name': 'Electronics'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categories(self):
        url = reverse('category-list-create')
        Category.objects.create(name='Electronics')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        category = Category.objects.create(name='Electronics')
        url = reverse('category-detail', args=[category.id])
        data = {'name': 'Updated Electronics'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        category = Category.objects.create(name='Electronics')
        url = reverse('category-detail', args=[category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductTests(APITestCase):

    def test_create_product(self):
        category = Category.objects.create(name='Electronics')
        url = reverse('product-list-create')
        data = {
            'name': 'Laptop',
            'description': 'A powerful laptop',
            'price': 999.99,
            'category': category.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_products(self):
        category = Category.objects.create(name='Electronics')
        Product.objects.create(name='Laptop', description='A powerful laptop', price=999.99, category=category)
        url = reverse('product-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        category = Category.objects.create(name='Electronics')
        product = Product.objects.create(name='Laptop', description='A powerful laptop', price=999.99, category=category)
        url = reverse('product-detail', args=[product.id])
        data = {
            'name': 'Gaming Laptop',
            'description': 'An even more powerful laptop',
            'price': 1199.99,
            'category': category.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        category = Category.objects.create(name='Electronics')
        product = Product.objects.create(name='Laptop', description='A powerful laptop', price=999.99, category=category)
        url = reverse('product-detail', args=[product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def patch(self, request, *args, **kwargs):
        logger.debug("PATCH data: %s", request.data)
        return super().patch(request, *args, **kwargs)
