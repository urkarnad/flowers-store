import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

#import FlowersShop
from FlowersShop.models import Flower, Category, Supplier


@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='1234')

@pytest.fixture
def api_client(client, user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def category(db):
    return Category.objects.create(name="test_category")

@pytest.fixture
def supplier(db):
    return Supplier.objects.create(name="test_supplier")

@pytest.fixture
def flower(db, category, supplier):
    return Flower.objects.create(
        name="test_flower",
        description="test_description",
        price=100,
        stock=18000,
        category=category,
        supplier=supplier,
    )