from rest_framework import generics
from .models import ShoppingList
from .serializers import ShoppingListSerializer, ShoppingListDetailSerializer
from cookbook_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ShoppingListView(generics.ShoppingListCreateAPIView):
    """View for listing and creating shopping list items."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return ShoppingList.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Save the owner of the item as the current user."""
        serializer.save(owner=self.request.user)


class ShoppingListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting an item."""
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return ShoppingList.objects.filter(owner=user)