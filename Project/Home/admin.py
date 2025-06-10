from django.contrib import admin
from .models import UserProfile,Room
# from .models import Room
# Register your models here.
# admin.site.register(UserProfile)
admin.site.register(Room)

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['first_name','email','address','gender','profile','documents','status','age','created_at','website_name']
    search_fields=['email']
    list_filter=['status']
    list_per_page =10

admin.site.register(UserProfile,UserProfileAdmin)