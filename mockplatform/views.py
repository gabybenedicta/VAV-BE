from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import ProductsSerializer
from .models import Products

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Welcome to the Mock Platform")

class ProductsViewSet(viewsets.ModelViewSet):
	queryset = Products.objects.all().order_by('date')
	serializer_class = ProductsSerializer
	