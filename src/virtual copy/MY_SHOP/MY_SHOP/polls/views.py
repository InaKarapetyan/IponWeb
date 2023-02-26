"""from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework import viewsets

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class StoreCategoryViewSet(viewsets.ModelViewSet):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer
"""