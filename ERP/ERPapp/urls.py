from django.urls import path
from ERPapp.views import Warehouse, Registration, Mainsite, Edit_product, Remove_produkt, Clients, Edit_client, Remove_client, Projects, Edit_project, Invoice__,Financial_Management



urlpatterns = [
    path('Warehouse/', Warehouse, name="Warehouse"),
    path('Main/', Mainsite, name="Mainsite"),
    path('Registration/', Registration, name="Registration"),
    path('Edit_product/<int:id>/', Edit_product, name="Edit_product"),
    path('Remove_produkt/<int:id>/', Remove_produkt, name="Remove_produkt"),
    path('Clients/', Clients, name="Clients"),
    path('Edit_client/<int:id>/', Edit_client, name="Edit_client"),
    path('Remove_client/<int:id>/', Remove_client, name="Remove_client"),
    path('Projects/', Projects, name="Projects"),
    path('Edit_project/<int:id>/', Edit_project, name="Edit_project"),
    path('Financial_Management', Financial_Management, name="Financial_Management"),
    path('Invoice', Invoice__, name="Invoice"),
]