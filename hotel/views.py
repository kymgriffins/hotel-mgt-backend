from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Role, User, Menu, Order, Reservation, Room
from .serializers import RoomSerializer, ReservationSerializer, RoleSerializer, OrderSerializer, MenuSerializer
# Create your views here.
# @csrf_exempt
# ROOMS 
@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        return Response({'Welcome Home'},status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','PATCH','DELETE'])
def room_details(request, pk):
    try:
        room = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = RoomSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# RESERVATIONS
@api_view(['GET', 'POST'])
def reservation_list(request):
    if request.method == "GET":
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print(request.data)
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','PATCH','DELETE'])
def reservation_details(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = ReservationSerializer(reservation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#MENUS 
@api_view(['GET', 'POST'])
def menu_list(request):
    if request.method == "GET":
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def menu_details(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = MenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ORDERS
@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == "GET":
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def order_details(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)