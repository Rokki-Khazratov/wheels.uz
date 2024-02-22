from rest_framework import serializers
from .models import Size, Category, Wheel, WheelImages


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class WheelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelImages
        fields = '__all__'


class WheelSerializer(serializers.ModelSerializer):
    size = SizeSerializer(many=True)
    images = WheelImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Wheel
        fields = '__all__'


    # def create(self, validated_data):
    #     sizes_data = validated_data.pop('size', [])
    #     images_data = validated_data.pop('images', [])
        
    #     wheel = Wheel.objects.create(**validated_data)

    #     for size_data in sizes_data:
    #         size, created = Size.objects.get_or_create(value=size_data['value'])
    #         wheel.size.add(size)

    #     for image_data in images_data:
    #         WheelImages.objects.create(wheel=wheel, **image_data)

    #     return wheel
