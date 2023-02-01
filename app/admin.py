from django.contrib import admin
from . models import seller,buyer,product,Contact
# Register your models here.
admin.site.register(seller)
admin.site.register(buyer)
admin.site.register(product)
admin.site.register(Contact)