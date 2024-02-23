from rest_framework import serializers
from .models import Detail, Category, UserProfile, Wheel, WheelImages
from django.contrib.auth.models import User







class DetailSerializer(serializers.ModelSerializer):
    wheel = serializers.CharField(source='wheel.name')

    class Meta:
        model = Detail
        fields = ['id', 'wheel_id', 'size','width','lenght', 'month_3_price', 'month_6_price', 'wheel'] 





# New serializer for details
class WheelDetailsSerializer(serializers.Serializer):
    def get_details(self, context):
        wheel_id = context.get('wheel_id')
        if wheel_id:
            filtered_details = Wheel.objects.get(pk=wheel_id).details.all()
        else:
            filtered_details = []
        return DetailSerializer(filtered_details, many=True).data



# Revised CategorySerializer
class CategorySerializer(serializers.ModelSerializer):
    wheels = WheelDetailsSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
    
    # def get_wheels(self, obj):
    #     return WheelDetailsSerializer(obj.wheels.filter(category_id=obj.pk), many=True).data
    





class WheelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelImages
        fields = '__all__'

        
class WheelSerializer(serializers.ModelSerializer):
    climate = serializers.CharField(source='get_climate_display')
    category = CategorySerializer(read_only=True)
    details = DetailSerializer(many=True, read_only=True)

    # def get_details(self, wheel):
    #     filtered_details = wheel.details.filter(wheel_id=wheel.id)
    #     return DetailSerializer(filtered_details, many=True).data
        
    def get_details(self, wheel):
        wheel_id = self.context.get('wheel_id')
        if wheel_id:
            filtered_details = wheel.details.filter(wheel_id=wheel_id)
        else:
            filtered_details = wheel.details.all() 
        return DetailSerializer(filtered_details, many=True).data

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