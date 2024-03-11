# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework import generics
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated


from django.db.models import Q
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .models import Detail, Category, Order, Wheel, WheelImages
from .serializers import DetailSerializer, CategorySerializer, OrderPostSerializer, OrderSerializer, PostDetailSerializer, WheelDetailSerializer, WheelSerializer, WheelImagesSerializer

# from django.contrib.auth.decorators import login_required
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})








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
    pagination_class = CustomPageNumberPagination  

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
            queryset = queryset.filter(details__length=details_length)

        if details_price_min:
            queryset = queryset.filter(details__price__gte=details_price_min)

        if details_price_max:
            queryset = queryset.filter(details__price__lte=details_price_max)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class WheelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wheel.objects.all().prefetch_related('details')
    serializer_class = WheelDetailSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.prefetch_related('wheels__images')
    serializer_class = CategorySerializer





# @login_required
# @permission_classes([IsAuthenticated])
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








# class DetailCreateAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = DetailSerializer(data=request.data)
#         if serializer.is_valid():
#             detail = serializer.save()
#             return Response(DetailSerializer(detail).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        detail_ids = request.data.get('details', [])
        details = Detail.objects.filter(id__in=detail_ids)

        order_serializer = OrderPostSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save(details=details)
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def bulk_create_wheels(request):
    wheels_data_list = request.data

    for serialized_data in wheels_data_list:
        details_data = serialized_data.pop('details', [])
        images_data = serialized_data.pop('images', [])

        wheel_serializer = WheelSerializer(data=serialized_data)

        if wheel_serializer.is_valid():
            wheel = wheel_serializer.save()

            # Associate details with the created wheel
            for detail_data in details_data:
                detail_data['wheel_id'] = wheel.id  # Associate the detail with the current wheel
                detail_serializer = PostDetailSerializer(data=detail_data)
                
                if detail_serializer.is_valid():
                    detail_serializer.save()
                else:
                    return Response(detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Associate images with the created wheel
            for image_data in images_data:
                image_data['wheel'] = wheel.id  # Associate the image with the current wheel
                image_serializer = WheelImagesSerializer(data=image_data)

                if image_serializer.is_valid():
                    image_serializer.save()
                else:
                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(wheel_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response("Данные успешно созданы", status=status.HTTP_201_CREATED)
