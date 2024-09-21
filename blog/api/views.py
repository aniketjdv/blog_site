from django.shortcuts import render
from api.models import BlogModel
from api.serializers import BlogSerializers
from rest_framework import viewsets
# Create your views here.

class BlogViewset(viewsets.ModelViewSet):
    queryset=BlogModel.objects.all()
    serializer_class=BlogSerializers