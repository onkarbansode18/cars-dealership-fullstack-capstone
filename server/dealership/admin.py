from django.contrib import admin
from .models import CarMake, CarModel, Dealership, Review

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name', 'country')

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'car_make', 'type', 'year')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name', 'car_make__name')

@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ('dealer_id', 'name', 'city', 'state', 'phone')
    list_filter = ('state', 'city')
    search_fields = ('name', 'city', 'state', 'zip')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'dealer', 'name', 'sentiment', 'created_at')
    list_filter = ('sentiment', 'dealer')
    search_fields = ('name', 'review')
