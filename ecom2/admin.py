from django.contrib import admin
# from .models import Product, Order, Customer, OrderItem, ShippingAddress
from .models import *


admin.site.register(Product)

admin.site.register(ProductGroup)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
