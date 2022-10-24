from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Questions)
admin.site.register(CategoryUser)
admin.site.register(Profile)
