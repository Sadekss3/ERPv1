from django.contrib import admin
from .models import Product, Client, Project, Invoice



admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Invoice)
