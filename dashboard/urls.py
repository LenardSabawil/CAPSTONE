from django.urls import path
from reservation.views import room_list, booking_view, approve_booking
from . import views

urlpatterns = [
    path('dashboard/', views.index, name="dashboard-index"),
    path('staff/', views.staff, name="dashboard-staff"),
    path('product/', views.product, name="dashboard-product"),
    path('product/delete/<int:pk>/', views.product_delete, name="dashboard-product-delete"),
    path('product/update/<int:pk>/', views.product_update, name="dashboard-product-update"),
    path('order/', views.order, name="dashboard-order"),
    path('reservation_list/', views.reservation_list, name="dashboard-reservation_list"),
    path('', views.dashboard, name="costumer-dashboard"),
    path('reservation/', views.reservation, name="costumer-reservation"),
    path('about/', views.about, name="costumer-about"),
    path('contact/', views.contact, name="costumer-contact"),
    path('rooms/', views.rooms, name="costumer-rooms"),
    path('events/', views.events, name="costumer-events"),
    path('room_list/', room_list, name='roomlist'),
    path('book/', booking_view, name='booking_view'),
    path('approve-booking/<int:booking_id>/', approve_booking, name='approve-booking'),
]