from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Role)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Reservation)
admin.site.register(Room)