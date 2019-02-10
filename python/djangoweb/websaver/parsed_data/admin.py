#parsed_data/admin.py
from django.contrib import admin

##model에서 BlogData를 import해옴.
from .models import BlogData
# Register your models here.

admin.site.register(BlogData)
