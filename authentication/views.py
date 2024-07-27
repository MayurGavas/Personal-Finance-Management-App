from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import SignUPViewSerializer, ResetPasswordViewSerializer, UserDetailSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class SignUp(APIView):
    def post(self, request):

        serializer = SignUPViewSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Logout(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]

    def post(self, request):
        # TODO : Make this Logout more robust. The access and refresh token should be invalid as soon as this post function runs.

        logout(request)
        # The logout(request) function in Django:
        # Clears Session Data: It removes the session data for the user, but it does not affect the authentication tokens (access and refresh tokens) directly.
        # Cookies: It removes the authentication cookies, which is useful for session-based authentication but not for token-based systems like JWT.

        return Response({'detail': 'This User is Logged Out'}, status=status.HTTP_200_OK)


class ResetPassword(APIView):

    # TODO : Make this Reset password logic more reliastic.
    def post(self, request):
        serializer = ResetPasswordViewSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']

            user = User.objects.filter(email=email).first()
            if not user:
                return Response({"details":"User Not Found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                user.set_password(new_password)
                user.save()

                response_user = UserDetailSerializer(user)
                return Response(response_user.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
