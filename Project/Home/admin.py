from django.contrib import admin
from .models import UserProfile,Room
# from .models import Room
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Room)