from rest_framework import serializers
from .models import Cart
from products.models import Product



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']


