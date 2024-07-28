from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserIncomeModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_income')
    source = models.CharField(max_length=50)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

