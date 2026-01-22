from django.urls import path
from .views import OrderListAPI

urlpatterns = [
    path('orders/', OrderListAPI.as_view()),
]
