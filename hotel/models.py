from django.db import models
from accounts.models import User
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
    availability = models.BooleanField(default=True)
    # image = models.URLField()

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
    # image = models.URLField()

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    food = models.ManyToManyField(Menu)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_time = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.customer.username} has been ordered {self.food.name} '
    
class Reviews(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    