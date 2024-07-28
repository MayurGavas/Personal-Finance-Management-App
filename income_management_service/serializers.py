from rest_framework.serializers import ModelSerializer
from .models import UserIncomeModel
from django.contrib.auth.models import User



class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]

class UserIncomeViewSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)
    def create(self, validated_data):
        user = self.context['request'].user
        income = UserIncomeModel.objects.create(user=user, **validated_data)
        return income

    class Meta:
        model = UserIncomeModel
        fields = ['id', 'source', 'amount', 'date', 'description', 'user']
