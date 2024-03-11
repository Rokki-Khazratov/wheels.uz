from rest_framework import serializers
from django.contrib.auth.models import User
from core.settings import BASE_URL
from urllib.parse import quote
from .models import Detail, Category, Order, UserProfile, Wheel, WheelImages




class ShortDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['size','width','length','month_3_price', 'month_6_price','month_9_price'] 





class PostDetailSerializer(serializers.ModelSerializer):
    wheel_id = serializers.PrimaryKeyRelatedField(queryset=Wheel.objects.all(), write_only=True)

    class Meta:
        model = Detail
        fields = ['id', 'wheel_id', 'size', 'width', 'length', 'price', 'month_3_price', 'month_6_price', 'month_9_price']
        read_only_fields = ['wheel']  # Make the wheel field read-only

    def create(self, validated_data):
        wheel_id = validated_data.pop('wheel_id', None)

        if not wheel_id:
            raise serializers.ValidationError("'wheel_id' must be provided.")

        wheel = wheel_id  # You might need to adjust this based on your model structure
        validated_data['wheel'] = wheel
        print(f"Creating Detail with data: {validated_data}")  # Add this line for debugging
        return super().create(validated_data)





class DetailSerializer(serializers.ModelSerializer):
    wheel = serializers.CharField(source='wheel.name', read_only=True)

    class Meta:
        model = Detail
        fields = ['id','wheel', 'size','width','length', 'price', 'month_3_price', 'month_6_price','month_9_price']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class WheelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelImages
        fields = '__all__'

        
class WheelSerializer(serializers.ModelSerializer):
    details = ShortDetailSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        first_image = WheelImages.objects.filter(wheel=obj).first()
        if first_image:
            return BASE_URL + first_image.image.url
        return None

    class Meta:
        model = Wheel
        fields = ['id', 'name', 'company', 'category', 'details', 'image']
        



class WheelDetailSerializer(serializers.ModelSerializer):
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
        fields = ['id', 'name','description','company', 'climate', 'category', 'details','images']

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