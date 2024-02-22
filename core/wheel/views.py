# views.py

from rest_framework import generics
from .models import Size, Category, Wheel, WheelImages
from .serializers import SizeSerializer, CategorySerializer, WheelSerializer, WheelImagesSerializer

class SizeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class SizeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class WheelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Wheel.objects.all()
    serializer_class = WheelSerializer

class WheelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wheel.objects.all()
    serializer_class = WheelSerializer

class WheelImagesListCreateAPIView(generics.ListCreateAPIView):
    queryset = WheelImages.objects.all()
    serializer_class = WheelImagesSerializer

class WheelImagesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WheelImages.objects.all()
    serializer_class = WheelImagesSerializer
