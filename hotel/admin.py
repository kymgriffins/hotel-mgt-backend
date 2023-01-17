from django.contrib import admin
from .models import Role, Menu, Order, Reservation, Room 
# Register your models here.

admin.site.register(Role)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Reservation)
admin.site.register(Room)