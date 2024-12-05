from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:pk>/', views.add_cart_item, name='add_cart_item'),
    path('cart/update/<int:pk>/', views.update_cart_item, name='update_cart_item'),
    path('cart/delete/<int:pk>/', views.delete_cart_item, name='delete_cart_item'),
    path('add/', views.add_ordered, name='add_ordered'),
    path('see/', views.view_ordered, name='view_ordered' )
]