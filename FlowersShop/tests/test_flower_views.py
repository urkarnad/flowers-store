from unicodedata import category

import pytest
from django.urls import reverse
from FlowersShop.models import Flower


@pytest.mark.django_db
def test_get_flower_view(api_client, flower):
    url = reverse('FlowersShop')
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()[0]['name'] == flower.name

@pytest.mark.django_db
def test_create_flower(api_client, category, supplier):
    url = reverse('FlowersShop')
    data = {
        'name': "Tulip",
        'description': "Tulip flower",
        'price': 50,
        'stock': 15000,
        'category': category.id,
        'supplier': supplier.id,
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert Flower.objects.filter(name="Tulip").exists()

@pytest.mark.django_db
def test_create_invalid_flower(api_client):
    url = reverse('FlowersShop')
    data = {
        'name': '',
        'price': 'meow'
    }
    response = api_client.post(url, data, content_type='application/json')
    assert response.status_code == 400

@pytest.mark.django_db
def test_get_flower_detail(api_client, flower):
    url = reverse('FlowersShopDetail', args=[flower.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()['name'] == flower.name

@pytest.mark.django_db
def test_get_flower_not_found(api_client):
    url = reverse('FlowersShopDetail', args=[1502])
    response = api_client.get(url)
    assert response.status_code == 404

@pytest.mark.django_db
def test_update_flower(api_client, flower, category, supplier):
    url = reverse('FlowersShopDetail', args=[flower.id])
    data = {
        'name': 'Updated flower',
        'description': flower.description,
        'price': flower.price,
        'stock': flower.stock,
        'category': flower.category.id,
        'supplier': flower.supplier.id,
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200
    flower.refresh_from_db()
    assert flower.name == 'Updated flower'

@pytest.mark.django_db
def test_delete_flower(api_client, flower):
    url = reverse('FlowersShopDetail', args=[flower.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Flower.objects.filter(id=flower.id).exists()

@pytest.mark.django_db
def test_delete_flower_not_found(api_client):
    url = reverse('FlowersShopDetail', args=[1502])
    response = api_client.delete(url)
    assert response.status_code == 404
