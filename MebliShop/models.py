from django.db import models
from django.urls import reverse
from django.utils import timezone

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category = models.ForeignKey(ProductCategory, related_name="sub_categories", on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sub_category_name

    def get_url(self):
        return reverse("MebliShop:sub_category_view", args=[self.id])

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, related_name="products", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=500)
    product_full_description = models.TextField(max_length=2000, blank=True)
    height = models.CharField(max_length=20, blank=True)
    width = models.CharField(max_length=20, blank=True)
    depth = models.CharField(max_length=20, blank=True)
    price = models.FloatField()
    count = models.IntegerField()
    sale_price = models.FloatField(null=True)
    image = models.ImageField(upload_to='products/main/%Y/%m/%d/', blank=True)
    additional_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    additional_image_2 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    additional_image_3 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    pub_date = models.DateField(default=timezone.now, blank=True)

    def is_available(self):
        return self.count > 0

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse("MebliShop:product_view", args=[self.id])


