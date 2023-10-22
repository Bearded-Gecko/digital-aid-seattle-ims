from django.urls import path, include
from .views import (inventory_list, 
                    per_product_view, 
                    add_product, 
                    delete_inventory, 
                    update_inventory, 
                    inventory_report,
                    donor_report)

urlpatterns = [
    path("", inventory_list, name = 'inventory_list'),
    path("per_product/<int:pk>", per_product_view, name = 'per_product'),
    path("add_inventory/", add_product, name = 'add_inventory'),
    path("delete/<int:pk>", delete_inventory, name = 'delete_inventory'),
    path("update/<int:pk>", update_inventory, name = 'update_inventory'),
    path("inventory_report/", inventory_report, name = "inventory_report" ),
    path("donor_report/", donor_report, name = "donor_report" )
]