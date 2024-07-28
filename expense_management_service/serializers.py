from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import UserExpensesModel


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]


class UserExpenseViewSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    def create(self, validated_data):
        user = self.context['request'].user
        expense = UserExpensesModel.objects.create(user=user, **validated_data)
        return expense

    class Meta:
        model = UserExpensesModel
        fields = ['id', 'category', 'amount', 'date', 'description', 'user']
