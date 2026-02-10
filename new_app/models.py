from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Rent', 'Rent'),
        ('Salary', 'Salary'),
        ('Entertainment', 'Entertainment'),
    ]

    title = models.CharField(max_length=100)
    amount = models.IntegerField(max_length=10)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


