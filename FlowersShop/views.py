from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.permissions import IsAdminOrReadOnly
from FlowersShop.serializers import *


class FlowersList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowersDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            flower = Flower.objects.get(pk=pk)
        except Flower.DoesNotExist:
            return Response({'error': 'Flower does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FlowerSerializer(flower)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            flower = Flower.objects.get(pk=pk)
        except Flower.DoesNotExist:
            return Response({'error': 'Flower does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FlowerSerializer(flower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            flower = Flower.objects.get(pk=pk)
        except Flower.DoesNotExist:
            return Response({'error': 'Flower does not exists'}, status=status.HTTP_404_NOT_FOUND)
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category does not exists'}, status=status.HTTP_404_NOT_FOUND)

        if Flower.objects.filter(category=category).exists():
            return Response({'error': 'Cannot delete category with an existing flowers'},
                            status=status.HTTP_400_BAD_REQUEST)

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SupplierList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({'error': 'Supplier does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({'error': 'Supplier does not exists'}, status=status.HTTP_404_NOT_FOUND)

        if Flower.objects.filter(supplier=supplier).exists():
            return Response({'error': 'Cannot delete supplier with an existing flowers'}, status=status.HTTP_400_BAD_REQUEST)

        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)