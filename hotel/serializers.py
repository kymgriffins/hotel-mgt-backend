from rest_framework import serializers
from .models import Role, User, Menu, Order, Reservation, Room, Image

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
        fields = '__all__'
class RoomSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'
        depth = 1
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'image']

class ReservationSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Reservation.objects.all())

    class Meta:
        model = Reservation
        fields = ['id','room', 'check_in_date', 'check_out_date', 'customer']
        depth = 1

    def create(self, validated_data):
        # Get the user ID from the validated data
        user_id = validated_data.pop('customer').id
        room_id = validated_data.pop('room').id

        # Create the reservation with the user ID
        reservation = Reservation.objects.create(customer_id=user_id,room_id=room_id, **validated_data)

        return reservation

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'description', 'images']
        depth =1

class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    food = MenuSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'food', 'customer', 'ordered_time', 'quantity', 'status']
        depth = 1



class RoleSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    
    class Meta:
        model = Role
        fields = ['id', 'name', 'users']
        depth = 1