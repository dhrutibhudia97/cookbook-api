from rest_framework import serializers
from .models import ShoppingList


class ShoppingListSerializer(serializers.ModelSerializer):
    """Serializer for the Item model."""
    class Meta:
        model = ShoppingList
        fields = ['id', 'name', 'quantity', 'created_at', 'updated_at']


class ShoppingListDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Item model."""
    class Meta:
        model = ShoppingList
        fields = ['id', 'name', 'quantity', 'created_at', 'updated_at']