from django.db import models as m


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

CLIMATE_CHOISES = [
    (1, 'Летние'),
    (2, 'Зимние'),
]


class Size(m.Model):
    value = m.IntegerField(choices=SIZE_CHOICES)

    def __str__(self):
        return str(self.value)


class Category(m.Model):
    name = m.CharField(max_length=255)
    sizes = m.ManyToManyField(Size)
    image = m.ImageField(upload_to="categories/")

    def __str__(self):
        return f"Car {self.name} - Sizes: {', '.join(str(size) for size in self.sizes.all())}"

class Wheel(m.Model):
    name = m.CharField(max_length=255)
    price = m.IntegerField()
    climate = m.IntegerField(choices=CLIMATE_CHOISES)
    size = m.ManyToManyField(Size)
    # category = m.ManyToManyField(Category)
    images = m.ManyToManyField('WheelImages', related_name='wheel_images', blank=True)


    def __str__(self):
        #For {self.category},
        return f"Car-{self.name} "

class WheelImages(m.Model) :
    wheel = m.ForeignKey(Wheel,on_delete=m.CASCADE)
    image = m.ImageField(upload_to="wheels/")

    def __str__(self):
        return self.wheel.name