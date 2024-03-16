from rest_framework import serializers
from django.contrib.auth.models import User
from core.settings import BASE_URL
from urllib.parse import quote
from .models import Detail, Category, Order, UserProfile, Wheel, WheelImages





class PostWheelSerializer(serializers.ModelSerializer):
    image = serializers.URLField(allow_null=True, allow_blank=True)

    class Meta:
        model = Wheel
        fields = ['id', 'name', 'company', 'description', 'climate', 'category', 'details', 'image']

    def create(self, validated_data):
        return Wheel.objects.create(**validated_data)


class PostWheelImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = WheelImages
        fields = ['image', 'wheel']

    def create(self, validated_data):
        image = validated_data.pop('image')
        wheel = validated_data.pop('wheel')
        instance = WheelImages.objects.create(image=image, wheel=wheel)
        return instance


class PostDetailSerializer(serializers.ModelSerializer):
    wheel_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Detail
        fields = ['id', 'wheel_id', 'size', 'width', 'length', 'price', 'month_3_price', 'month_6_price', 'month_9_price']
        read_only_fields = ['wheel']  

    def create(self, validated_data):
        wheel_id = validated_data.pop('wheel_id', None)

        if wheel_id is None:
            raise serializers.ValidationError("'wheel_id' must be provided.")

        try:
            wheel = Wheel.objects.get(id=wheel_id)
        except Wheel.DoesNotExist:
            raise serializers.ValidationError("Invalid 'wheel_id' provided.")

        validated_data['wheel'] = wheel

        # Create the detail and associate it with the wheel
        detail = super().create(validated_data)
        wheel.details.add(detail)  

        return detail





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
    








class ShortDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['size','width','length','month_3_price', 'month_6_price','month_9_price'] 

class DetailSerializer(serializers.ModelSerializer):
    wheel = serializers.CharField(source='wheel.name', read_only=True)

    class Meta:
        model = Detail
        fields = ['id','wheel', 'size','width','length', 'price', 'month_3_price', 'month_6_price','month_9_price']




class CategorySerializer(serializers.ModelSerializer):
    sizes = serializers.SerializerMethodField()

    def get_sizes(self, obj):
        return [size.name for size in obj.sizes.all()]

    class Meta:
        model = Category
        fields = '__all__'

    

class WheelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelImages
        fields = '__all__'

        
class WheelSerializer(serializers.ModelSerializer):
    details = ShortDetailSerializer(many=True, read_only=True)
    one_image = serializers.SerializerMethodField()

    def get_one_image(self, obj):
        first_image = WheelImages.objects.filter(wheel=obj).first()
        if first_image:
            return BASE_URL + first_image.image.url
        return None

    class Meta:
        model = Wheel
        fields = ['id', 'name', 'company', 'category', 'details', 'image','one_image']
        



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
        fields = ['id', 'name','description','company', 'image','climate', 'category', 'details','images']

class OrderSerializer(serializers.ModelSerializer):
    details = DetailSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'





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