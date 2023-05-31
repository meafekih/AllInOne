from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from .models import Blog
from .serializer import blogSerializer

def home(request):
    return HttpResponse("Welcome")


class blogApi(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)