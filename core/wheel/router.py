from django.urls import path
from .views import (
    DetailListCreateAPIView, DetailRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, OrderCreateAPIView, OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView,
    WheelListCreateAPIView, WheelRetrieveUpdateDestroyAPIView,
)

urlpatterns = [

    path('categories/', CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),


    path('details/', DetailListCreateAPIView.as_view(), name='Detail-list-create'),
    path('details/<int:pk>/', DetailRetrieveUpdateDestroyAPIView.as_view(), name='Detail-retrieve-update-destroy'),

    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),

    path('wheels/', WheelListCreateAPIView.as_view(), name='wheel-list-create'),
    path('wheels/<int:pk>/', WheelRetrieveUpdateDestroyAPIView.as_view(), name='wheel-retrieve-update-destroy'),


    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update-destroy'),


    path('create_order/', OrderCreateAPIView.as_view(), name='create_order'),
]
    # path('create_detail/', DetailCreateAPIView.as_view(), name='create_detail'),


