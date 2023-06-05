from django.urls import path
from .views import order_form, order_success, order_dashboard

urlpatterns = [
    path('', order_form, name = "order_form"),
    path('success/', order_success, name = 'order_success'),
    path('order_dashboard/', order_dashboard, name = "viz")
]
