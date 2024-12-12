from django.shortcuts import render
from rest_framework import viewsets
from ordering.models import  Comment
from .serializers import  CommentSerializer 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
