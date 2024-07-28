from django.urls import path , include
from . import views


urlpatterns = (

    path('add-expense/', views.UserExpenseView.as_view(), name = 'add-expense'),
    path('get-expense/', views.GetUserExpenseView.as_view(), name = "get-user-expense"),


)