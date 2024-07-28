from django.shortcuts import render
from .models import UserExpensesModel
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User

from .serializers import UserExpenseViewSerializer


class UserExpenseView(generics.GenericAPIView,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserExpenseViewSerializer

    def get_queryset(self):
        user = self.request.user
        return UserExpensesModel.objects.filter(user = user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self,  request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # TODO : Handle Partial Update here
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        #return self.get_queryset().filter(pk = self.kwargs['pk']).first()   #--  OK

        queryset = self.get_queryset()
        return generics.get_object_or_404(queryset, pk=self.kwargs['pk'])   #--- Correct Way




