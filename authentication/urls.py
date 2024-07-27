from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('sign-up/', views.SignUp.as_view(), name='signup'),
    path('sign-up/<int:pk>/', views.SignUp.as_view(), name='delete-user'),

    path('login/', TokenObtainPairView.as_view(), name='login',),
    path('token/refresh/', TokenRefreshView.as_view(), name ='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('logout/', views.Logout.as_view(), name='logout'),

    path('reset-password/', views.ResetPassword.as_view(), name='reset-password')

]




