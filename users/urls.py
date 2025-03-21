from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registrantion_api_view),
    path('authorization/', views.authorization_api_view),
    path('confirm', views.SMSCodeConfirm),
]
