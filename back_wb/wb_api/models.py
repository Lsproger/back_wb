from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=500, blank=True, default='')
    price = models.FloatField(blank=True, default=0.00) 
    discount = models.IntegerField(blank=True, default=0)
    count = models.IntegerField(blank=True, default=0)
    image_url = models.URLField(max_length=500, blank=True, default='')

    class Meta:
        ordering = ['id']
        # app_label = 'back-wb.wb-api'

