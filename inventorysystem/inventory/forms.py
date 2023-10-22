from django.forms import ModelForm
from .models import Inventory

class AddInventoryForm(ModelForm):
    class Meta: #meta class
        model = Inventory
        fields = ['donor_name', 'item_type', 'amount', 'date', 'location']

class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['donor_name', 'item_type', 'amount', 'date', 'location']