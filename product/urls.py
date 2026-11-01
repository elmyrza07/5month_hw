from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),

    path('products/', views.ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product_detail'),

    path('reviews/', views.ReviewListAPIView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetailAPIView.as_view(), name='review_detail'),
]