from rest_framework import generics
from .models import ShoppingList
from .serializers import ShoppingListSerializer, ShoppingListDetailSerializer
from cookbook_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ShoppingListView(generics.ListCreateAPIView):
    """
    View for creating shopping list item if user is logged in.
    """
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return ShoppingList.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ShoppingListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieving, updating, and deleting a shoppinglist item.
    """
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return ShoppingList.objects.filter(owner=user)