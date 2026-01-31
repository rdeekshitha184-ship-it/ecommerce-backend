from django.urls import path
from .views import CartView, AddToCartView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cart/add/', AddToCartView.as_view()),
]
