from django.db import models
from accounts.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image')

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
    images = CloudinaryField('Rooms',null=True, default=None, blank=True)


    # image = models.URLField() + change availability to choices

    def __str__(self):
        return f"{self.room_number}"

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(auto_now_add=True)
    check_out_date = models.DateTimeField()
    def __str__(self):
        return f'{self.customer.username} has reserved room number {self.room.room_number}'
class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    images = CloudinaryField('Menus', null=True, default=None, blank=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    items = models.ManyToManyField(Menu, through='OrderItem')
    def __str__(self):
        return f'{self.customer.username} has ordered {self.items.count()} items'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
  

    def __str__(self):
        return f'{self.quantity} of {self.food.name} in order {self.order.id}'

class Reviews(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500, null=True, blank=True)
    