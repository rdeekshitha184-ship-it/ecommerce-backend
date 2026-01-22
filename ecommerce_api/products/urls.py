from django.urls import path
from .views import ProductListAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view()),
]
