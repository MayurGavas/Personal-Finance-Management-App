from django.shortcuts import render
from .models import UserExpensesModel
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User

from .serializers import AddUserExpenseViewSerializer, GetUserExpenseViewSerializer


class UserExpenseView(generics.GenericAPIView, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = UserExpensesModel.objects.all()
    serializer_class = AddUserExpenseViewSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetUserExpenseView(generics.GenericAPIView, mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = UserExpensesModel.objects.all()
    serializer_class = GetUserExpenseViewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)
