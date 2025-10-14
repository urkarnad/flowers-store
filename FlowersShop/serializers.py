from rest_framework import serializers
from .models import Flower, Category, Supplier


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class FlowerSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Flower
        fields = '__all__'
