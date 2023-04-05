from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'roles']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'image']


class RoomSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Room
        fields = '__all__'
        depth = 1


class ReservationSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Reservation
        fields = ['id', 'room', 'check_in_date', 'check_out_date', 'customer']
        depth = 1

    def create(self, validated_data):
        # Get the user and room objects from the validated data
        customer = validated_data.pop('customer')
        room = validated_data.pop('room')

        # Create the reservation object with the user and room objects
        reservation = Reservation.objects.create(customer=customer, room=room, **validated_data)

        return reservation


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'




class RoleSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'users']
        depth = 1
