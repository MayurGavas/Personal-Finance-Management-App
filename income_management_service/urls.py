from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('income',views.UserIncomeView,basename='income_details')


urlpatterns = [
    path('',include(router.urls))
]