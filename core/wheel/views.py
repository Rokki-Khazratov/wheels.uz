# views.py
from django.db.models import Q
from rest_framework import generics
from .models import Detail, Category, Order, Wheel, WheelImages
from .serializers import DetailSerializer, CategorySerializer, OrderSerializer, WheelSerializer, WheelImagesSerializer

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
    serializer_class = WheelSerializer

    def get_queryset(self):
        queryset = Wheel.objects.all().prefetch_related('details')

        climate = self.request.query_params.get('climate', None)
        category_id = self.request.query_params.get('category_id', None)
        details_size = self.request.query_params.get('details_size', None)
        details_width = self.request.query_params.get('details_width', None)
        details_length = self.request.query_params.get('details_length', None)
        details_price_min = self.request.query_params.get('details_price_min', None)
        details_price_max = self.request.query_params.get('details_price_max', None)

        if climate:
            queryset = queryset.filter(climate=climate)

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if details_size:
            queryset = queryset.filter(details__size=details_size)

        if details_width:
            queryset = queryset.filter(details__width=details_width)

        if details_length:
            queryset = queryset.filter(details__lenght=details_length)

        if details_price_min:
            queryset = queryset.filter(details__price__gte=details_price_min)

        if details_price_max:
            queryset = queryset.filter(details__price__lte=details_price_max)

        return queryset


class WheelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wheel.objects.all().prefetch_related('details')
    serializer_class = WheelSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.prefetch_related('wheels__images')
    serializer_class = CategorySerializer



class OrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()

        category_id = self.request.query_params.get('category_id', None)
        category_name = self.request.query_params.get('category_name', None)
        is_checked = self.request.query_params.get('is_checked', None)

        if category_id:
            queryset = queryset.filter(details__wheel__category_id=category_id)

        if category_name:
            queryset = queryset.filter(details__wheel__category__name=category_name)
        
        if is_checked is not None:
            queryset = queryset.filter(is_checked=is_checked.lower() == 'true')

        return queryset

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer