from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(
            categories, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404({'message': 'دسته بندی مورد نظر یافت نشد',
                          'status': status.HTTP_404_NOT_FOUND})

        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404({'message': 'فیلم مورد نظر یافت نشد',
                          'status': status.HTTP_404_NOT_FOUND})

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


class FileListView(APIView):
    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(
            files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):
    def get(self, request, product_id, pk):
        try:
            file = File.objects.get(pk=pk, product_id=product_id)
        except Product.DoesNotExist:
            raise Http404({'message': 'فایل مورد نظر یافت نشد',
                          'status': status.HTTP_404_NOT_FOUND})

        serializer = FileSerializer(file, context={'request': request})
        return Response(serializer.data)
