from django.db import models
from djmoney.models.fields import MoneyField

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
        
class News(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    photo = models.FileField(upload_to='images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.pk} {self.title}"
    
    
    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Products'


class Product_category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'P_Types'


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Product_category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Types'
        verbose_name_plural = 'Types'












