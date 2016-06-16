from __future__ import unicode_literals

from django.db import models

libel = "{title} / {price} euro"


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image', blank=True, verbose_name="image")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return libel.format(title=self.title, price=str(self.price))
