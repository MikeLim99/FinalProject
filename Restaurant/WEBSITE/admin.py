from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Reservation, Product, CustomerFeedback


admin.site.register(CustomerFeedback)
admin.site.unregister(Group)
admin.site.register(Product)
admin.site.register(Reservation)