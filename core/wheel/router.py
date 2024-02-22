from django.urls import path
from .views import (
    SizeListCreateAPIView, SizeRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    WheelListCreateAPIView, WheelRetrieveUpdateDestroyAPIView,
    WheelImagesListCreateAPIView, WheelImagesRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('sizes/', SizeListCreateAPIView.as_view(), name='size-list-create'),
    path('sizes/<int:pk>/', SizeRetrieveUpdateDestroyAPIView.as_view(), name='size-retrieve-update-destroy'),

    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),

    path('wheels/', WheelListCreateAPIView.as_view(), name='wheel-list-create'),
    path('wheels/<int:pk>/', WheelRetrieveUpdateDestroyAPIView.as_view(), name='wheel-retrieve-update-destroy'),

    path('wheel-images/', WheelImagesListCreateAPIView.as_view(), name='wheel-images-list-create'),
    path('wheel-images/<int:pk>/', WheelImagesRetrieveUpdateDestroyAPIView.as_view(), name='wheel-images-retrieve-update-destroy'),
]
