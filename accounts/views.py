from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer,LoginSerializer,UserSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class SignInAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print(user.id)
        if user:
            user_token=Token.objects.get_or_create(user=user)[0]#creating token for user every time he/she login

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": user_token.key
        })
