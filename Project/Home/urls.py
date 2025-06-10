from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="MainPage"),
    path("properties/",views.properties,name="propertiesPage"),
    path("propertydetails/",views.propertydetails,name="propertyDetailsPage"),
    path("contact/",views.contact,name="contactPage"),
]
