from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import Product
from app.serializer import ProductSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def home(request):
    return Response({"message": "Hello for today! See you tomorrow!"})

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def products_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_view(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
