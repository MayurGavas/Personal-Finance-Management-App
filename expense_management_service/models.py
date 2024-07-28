from django.db import models
from django.contrib.auth.models import models, User


class UserExpensesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_expense')
    category = models.CharField(max_length=30)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)


