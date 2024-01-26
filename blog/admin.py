from django.contrib import admin


from .models import Category, News, Product_category


admin.site.register(Category)
admin.site.register(News)
admin.site.register(Product_category)