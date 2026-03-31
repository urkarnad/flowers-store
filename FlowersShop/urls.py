from django.urls import path
from .views import *

urlpatterns = [
    path('flowers/', FlowersList.as_view(), name='FlowersShop'),
    path('flowers/<int:pk>/', FlowersDetail.as_view(), name='FlowersShopDetail'),

    path('categories/', CategoryList.as_view(), name='CategoryList'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='CategoryDetail'),

    path('suppliers/', SupplierList.as_view(), name='SupplierList'),
    path('suppliers/<int:pk>/', SupplierDetail.as_view(), name='SupplierDetail'),
    ]
