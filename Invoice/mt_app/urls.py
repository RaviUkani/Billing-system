from django.urls import path
from . import views

urlpatterns = [
    path('customer_list/',views.customer_list, name='customer_saved'),
    path('order_list/',views.order_list, name='order_saved'),
    path('item_list/',views.item_list, name='item_saved'),
    path('home/',views.home, name='home_saved'),
    path('invoice/<int:pk>',views.invoice, name='invoice_pk'),
    path('customer_input/',views.customer_input, name='customer_input'),
    path('order_input/',views.order_input, name='order_input'),
    path('item_input/',views.item_input, name='item_input'),
]
