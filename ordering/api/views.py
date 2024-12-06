from django.shortcuts import render
from rest_framework import viewsets
from ordering.models import Ordering, Comment
from .serializers import OrderingSerializer, CommentSerializer

class OrderingViewSet(viewsets.ModelViewSet):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
