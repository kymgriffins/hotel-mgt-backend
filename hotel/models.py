from datetime import timezone
from django.db import models
from accounts.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name




class Room(models.Model):
    AVAILABILITY_CHOICES = (
        ('available', 'AVAILABLE'),
        ('reserved', 'RESERVED'),
    )
    description= models.TextField(max_length=500)
    room_number = models.PositiveIntegerField(unique=True)
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    max_occupancy = models.PositiveSmallIntegerField()
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default='available')
    images = models.ManyToManyField('RoomImage', blank=True, related_name="RoomImage")


    # image = models.URLField() + change availability to choices

    def __str__(self):
        return f"{self.room_number}"
    def reserve(self, customer, check_in_date, check_out_date):
        if self.is_available(check_in_date, check_out_date) and not Reservation.is_active(self):
            self.availability = 'reserved'
            self.save()
            Reservation.objects.create(
                room=self,
                customer=customer,
                check_in_date=check_in_date,
                check_out_date=check_out_date
            )
            return True
        else:
            return False
    
class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = CloudinaryField("RoomImage", null=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.room:
            self.room.images.add(self)
        

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(auto_now_add=True)
    check_out_date = models.DateTimeField()
    def __str__(self):
        return f'{self.customer.username} has reserved room number {self.room.room_number}'
    def is_active(cls, room):
        now = timezone.now()
        return cls.objects.filter(room=room, check_in_date__lte=now, check_out_date__gt=now).exists()

class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    images = models.ManyToManyField('MenuImage', blank=True, related_name="MenuImage")
    def __str__(self):
        return self.name
class MenuImage(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    image = CloudinaryField("MenuImages", null=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.menu:
            self.menu.images.add(self)
        
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    items = models.ManyToManyField('OrderItem', blank=True, related_name="orders")
    def __str__(self):
        return f'{self.customer.username} has ordered {self.items.count()} items'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.order:
            self.order.items.add(self)
  

    def __str__(self):
        return f'{self.quantity} of {self.food.name} in order {self.order.id}'

class Reviews(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500, null=True, blank=True)
    