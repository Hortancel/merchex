from django.contrib import admin
from .models import Band
from .models import Listing


class BandAdmin(admin.ModelAdmin):
    list_display =('name' ,'year_formed','genre')

admin.site.register(Band)


class ListingAdmin(admin.ModelAdmin):
    list_display =('title','band')
    
admin.site.register(Listing)