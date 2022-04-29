from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PostAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
