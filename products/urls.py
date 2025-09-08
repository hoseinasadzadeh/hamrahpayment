from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(),
         name='category-detail'),

    path('movie/', views.ProductListView.as_view(), name='product-list'),
    path('movie/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('movie/<int:product_id>/files/',
         views.FileListView.as_view(), name='file-list'),
    path('movie/<int:product_id>/files/<int:pk>/',
         views.FileDetailView.as_view(), name='file-detail'),
]
