from django.db import models as m
from django.contrib.auth.models import User



SIZE_CHOICES = [
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
]

class Detail(m.Model):
    category = m.ForeignKey('Wheel', on_delete=m.CASCADE)
    size = m.IntegerField(choices=SIZE_CHOICES)
    price = m.IntegerField()

    @property
    def month_3_price(self):
        if self.price:
            return round(self.price / 3, 2) 
        else:
            return None 

    @property
    def month_6_price(self):
        if self.price:
            return round(self.price / 6, 2) 
        else:
            return None 

    def __str__(self):
        return f"{self.category.name} - Размер: {self.value}"

    

class Category(m.Model):
    name = m.CharField(max_length=255)
    image = m.ImageField(upload_to="categories/")

    def __str__(self):
        return f"Автомобиль {self.name}"

class Wheel(m.Model):
    name = m.CharField(max_length=255)
    climate = m.IntegerField(choices=CLIMATE_CHOICES)
    category = m.ForeignKey(Category, on_delete=m.CASCADE)
    images = m.ManyToManyField('WheelImages', related_name='wheel_images', blank=True)

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