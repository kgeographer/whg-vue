from django.contrib import admin

from .models import Place

# admin.site.register(Place)

# Define the admin class
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('placeid','src_id','title','dataset')

# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('geonameid','gnlabel','iso','un')
