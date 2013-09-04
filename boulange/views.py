from django.views.generic import ListView
from .models import InventoryItem

class InventoryList(ListView):
    model = InventoryItem