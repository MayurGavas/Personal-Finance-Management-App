from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserIncomeViewSerializer
from . models import UserIncomeModel



class UserIncomeView(ModelViewSet):

    permission_classes = [IsAuthenticated ]
    authentication_classes = [JWTAuthentication ]
    serializer_class = UserIncomeViewSerializer

    def get_queryset(self):
        user = self.request.user
        return UserIncomeModel.objects.filter(user = user)


    def get_object(self):
        queryset = self.get_queryset()
        return generics.get_object_or_404(queryset, pk=self.kwargs['pk'])   #--- Correct Way





