from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrantionAPIView.as_view()),
    path('authorization/', views.AuthorizationAPIView.as_view()),
    path('confirm/', views.SMSCodeConfirm.as_view()),
]
