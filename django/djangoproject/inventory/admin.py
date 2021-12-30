from django.contrib import admin

# Register your models here.
from .models import Product,Supplier,Customer,Order,PO,PS

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(PO)
admin.site.register(PS)