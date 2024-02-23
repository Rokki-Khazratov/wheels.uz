from rest_framework import serializers
from .models import Size, Category, UserProfile, Wheel, WheelImages
from django.contrib.auth.models import User



class SizeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name') 
    class Meta:
        model = Size
        fields = ['category','price','value']


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
    details = SizeSerializer(many=True, read_only=True, source='details.all')

    class Meta:
        model = Wheel
        fields = ['id', 'name', 'climate', 'category', 'details']

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




class UserAbstract(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'phone_number']


class UserSerializer(serializers.ModelSerializer):
    profile = UserAbstract(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует.')

        if len(password) < 8:
            raise ValidationError('Пароль должен содержать более 8 символов.')
        return data

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(**validated_data)

        profile, created = UserProfile.objects.get_or_create(user=user, defaults=profile_data)

        if not created:
            for key, value in profile_data.items():
                setattr(profile, key, value)
            profile.save()

        return user