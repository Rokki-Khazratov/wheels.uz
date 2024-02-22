from django.db import models as m


SIZE_CHOICES = [
    # (1, '1'),
    # (2, '2'),
    # (3, '3'),
    # (4, '4'),
    # (5, '5'),
    # (6, '6'),
    # (7, '7'),
    # (8, '8'),
    # (9, '9'),
    # (10, '10'),
    # (11, '11'),
    # (12, '12'),
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


class Category(m.Model):
    name = m.CharField(max_length=255)
    image = m.ImageField(upload_to="categories/")

    def __str__(self) -> str:
        return self.name

class Wheel(m.Model):
    name = m.CharField(max_length=255)
    price = m.IntegerField()
    size = m.IntegerField(choices=SIZE_CHOICES)
    climate = m.IntegerField(choices=CLIMATE_CHOISES)
    category = m.ForeignKey(Category,on_delete=m.CASCADE)
    images = m.ManyToManyField('WheelImages', related_name='wheel_images', blank=True)


    def __str__(self):
        return f"For {self.category},Car-{self.name} "

class WheelImages(m.Model) :
    wheel = m.ForeignKey(Wheel,on_delete=m.CASCADE)
    image = m.ImageField(upload_to="wheels/")

    def __str__(self):
        return self.wheel.name