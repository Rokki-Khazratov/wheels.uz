# views.py

from rest_framework import generics
from .models import Detail, Category, Wheel, WheelImages
from .serializers import DetailSerializer, CategorySerializer, WheelSerializer, WheelImagesSerializer

class DetailListCreateAPIView(generics.ListCreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class DetailRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer



class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.select_related('image')

    def get_object(self):
        category = super().get_object()
        return category


class WheelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Wheel.objects.all().prefetch_related('details')
    serializer_class = WheelSerializer

class WheelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wheel.objects.all().prefetch_related('details')
    serializer_class = WheelSerializer




class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.prefetch_related('wheels__images')
    serializer_class = CategorySerializer