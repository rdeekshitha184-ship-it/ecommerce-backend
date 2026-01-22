from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS = (
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS)
