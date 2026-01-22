from django.urls import path
from .views import CartListAPI

urlpatterns = [
    path('cart/', CartListAPI.as_view()),
]
