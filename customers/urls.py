from django.urls import path
from account import views as AccountViews
from . import views

urlpatterns = [
    path('', AccountViews.custDashboard, name='customer'),
    path('profile/', views.cprofile, name='cprofile'),
    path('my_orders/', views.my_orders, name='customer_my_order'),
    path('order_detail/<int:order_number>', views.order_detail, name='order_detail'),
]
