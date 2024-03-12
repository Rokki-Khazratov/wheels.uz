from django.db import models as m
from django.contrib.auth.models import User



def order_image_path(instance, filename):
    return f'orders/passports/{instance.id}/image.jpg'

SIZE_CHOICES = [
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
    (17, '17'),
    (18, '18'),
    (19, '19'),
    (20, '20'),
]

CLIMATE_CHOICES = [
    (1, 'Летние'),
    (2, 'Зимние'),
    (3, 'Универсальный'),
]

class Detail(m.Model):
    wheel = m.ForeignKey('Wheel', on_delete=m.CASCADE,blank=True) 
    size = m.IntegerField(choices=SIZE_CHOICES)
    width = m.IntegerField(blank=True)
    length = m.IntegerField(blank=True)
    price = m.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    month_3_price = m.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    month_6_price = m.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    month_9_price = m.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # @property
    # def month_3_price(self):
    #     if self.price:
    #         return round(self.price / 3, 2) 
    #     else:
    #         return None 

    # @property
    # def month_6_price(self):
    #     if self.price:
    #         return round(self.price / 6, 2) 
    #     else:
    #         return None 

    def __str__(self):
        return f"{self.wheel.name} - Размер: {self.size}"

    

class Category(m.Model):
    name = m.CharField(max_length=255)
    image = m.ImageField(upload_to="categories/")

    def __str__(self):
        return f"Автомобиль {self.name}"

class Wheel(m.Model):
    name = m.CharField(max_length=255, default="Unknown")
    company = m.CharField(max_length=255)
    description = m.TextField(blank=True)
    climate = m.IntegerField(choices=CLIMATE_CHOICES,blank=True,null=True)
    category = m.ForeignKey(Category, on_delete=m.CASCADE,related_name='wheels',blank=True,null=True)
    details = m.ManyToManyField('Detail', related_name='wheels',blank=True)
    images = m.ManyToManyField('WheelImages', related_name='wheel_images', blank=True)
    image = m.URLField(blank=True, null=True)

    def __str__(self):
        return f"Автомобиль-{self.name} "

class WheelImages(m.Model):
    wheel = m.ForeignKey(Wheel, on_delete=m.CASCADE)
    image = m.ImageField(upload_to="wheels/")

    def __str__(self):
        return self.wheel.name
    


class UserProfile(m.Model):
    user = m.OneToOneField(User, on_delete=m.CASCADE)
    name = m.CharField(max_length=100,null=True, blank=True)
    phone_number = m.CharField(max_length=15,null=True, blank=True)

    def __str__(self):
        return str(self.user) 

class Order(m.Model):
    full_name = m.CharField(max_length=100)
    phone_number = m.CharField(max_length=20)
    passport_image = m.FileField(upload_to=order_image_path, blank=True, null=True)

    longitude = m.CharField(max_length=100)
    latitude = m.CharField(max_length=100)
    adress = m.CharField(max_length=100)

    is_checked = m.BooleanField(default=False)

    details = m.ManyToManyField(Detail, related_name='orders', blank=True)
    # quantity = m.PositiveSmallIntegerField()

    def __str__(self):
        return f" {self.full_name} :  {self.phone_number}"