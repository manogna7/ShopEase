from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet, product_list
from . import views


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('products/', product_list, name='product-list-html'),  # Correct path for HTML view
    path('api/products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('api/categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail')

]
