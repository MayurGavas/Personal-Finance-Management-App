from django.urls import path , include
from . import views


urlpatterns = (

    path('expense/', views.UserExpenseView.as_view(), name = 'add-expense'),
    path('expense/<int:pk>/', views.UserExpenseView.as_view(), name = 'add-expense'),

)