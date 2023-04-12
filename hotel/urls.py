from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('rooms/', views.room_list, name='room-list'),
    path('room/<int:pk>/', views.room_details, name='room-details'),
    path('reservations/', views.reservation_list, name='reservation-list'),
    path('reservation/<int:pk>/', views.reservation_details, name='reservation-details'),
    path('menu/', views.menu_list, name='menu-list'),
    path('menu/<int:pk>/', views.menu_details, name='menu-details'),
    path('orders/', views.order_list, name='order-list'),
    path('orders/<int:pk>/', views.order_details, name='orders-details'),
    path('orderitems/', views.add_order_item, name='add-order-item'),
    path('orders/<int:order_pk>/<int:item_pk>/', views.order_item_details, name='order-item-details'),
    path('roomimages/', views.room_images, name='room_images-list'),
    path('menuimages/', views.menu_images, name='menu_images-details'),
]
