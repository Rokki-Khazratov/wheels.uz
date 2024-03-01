from rest_framework import serializers
from .models import Detail, Category, Order, UserProfile, Wheel, WheelImages
from django.contrib.auth.models import User
from core.settings import BASE_URL
from urllib.parse import quote





class DetailSerializer(serializers.ModelSerializer):
    wheel = serializers.CharField(source='wheel.name')

    class Meta:
        model = Detail
        fields = ['id','wheel', 'size','width','lenght', 'month_3_price', 'month_6_price'] 



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class WheelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelImages
        fields = '__all__'

        
class WheelSerializer(serializers.ModelSerializer):
    climate = serializers.CharField(source='get_climate_display')
    category = CategorySerializer(read_only=True)
    details = DetailSerializer(many=True, read_only=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = WheelImages.objects.filter(wheel=obj)
        serialized_images = WheelImagesSerializer(images, many=True).data
        for image_data in serialized_images:
            image_data['image'] = BASE_URL + image_data['image']

        return serialized_images


    class Meta:
        model = Wheel
        fields = ['id', 'name','description', 'climate', 'category', 'details','images']

class OrderSerializer(serializers.ModelSerializer):
    details = DetailSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderPostSerializer(serializers.ModelSerializer):
    details = serializers.PrimaryKeyRelatedField(
        queryset=Detail.objects.all(), many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
    
        if representation['passport_image']:
            representation['passport_image'] = quote(representation['passport_image'])

        return representation




# class UserAbstract(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'phone_number']


# class UserSerializer(serializers.ModelSerializer):
#     profile = UserAbstract(required=False)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password', 'profile']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         if User.objects.filter(username=username).exists():
#             raise ValidationError('Пользователь с таким именем уже существует.')

#         if len(password) < 8:
#             raise ValidationError('Пароль должен содержать более 8 символов.')
#         return data

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile', {})
#         user = User.objects.create_user(**validated_data)

#         profile, created = UserProfile.objects.get_or_create(user=user, defaults=profile_data)

#         if not created:
#             for key, value in profile_data.items():
#                 setattr(profile, key, value)
#             profile.save()

#         return user