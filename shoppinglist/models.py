from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    """
    For adding items and quantities to the shopping list.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.quantity}"

    class Meta:
        ordering = ['-created_at']
