from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from . import serializers, models
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
import random
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = serializers.UserAuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)   
        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.create(user=user)
            return Response(data={'token': token.key}, status=200)
        return Response(status=status.HTTP_401_UNAUTHORIZED,data={'User credentials are wrong'})


class RegistrantionAPIView(APIView):
    def post(self, request):
        serializer = serializers.UserRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        user = User.objects.create_user(
                username=serializer.validated_data.get('username'),
                password=serializer.validated_data.get('password'),
                email=serializer.validated_data.get('email'),
                is_active=False
        )
        code = ''.join([str(random.randint(0, 9) for i in range(6))])
        models.SMSCode.objects.create(code=code, user=user)
        send_mail(
                'Registration code',
                message=code,
                from_email='<EMAIL>',
                recipient_list=[user.email]
        )
        return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)

class SMSCodeConfirm(APIView):
    def post(self, request):
        serializer = serializers.SMSCodeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        sms_code = serializer.validated_data.get('sms_code')
        try:
            sms_code = models.SMSCode.objects.get(code=sms_code)
        except models.SMSCode.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Code not found'})
        sms_code.user.is_active = True
        sms_code.user.save()
        sms_code.delete()
        return Response(status=status.HTTP_200_OK)
            
