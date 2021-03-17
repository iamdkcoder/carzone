from django.contrib import admin
from .models import car
from django.utils.html  import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src ="{}" width ="50" style= "border-radius: 40px"/>', format(object.car_photo.url))
    thumbnail.short_description = 'car photo'
    list_display = ('id' ,'thumbnail' , 'car_title' , 'color', 'body_style','year', 'city' , 'fuel_type' , 'created_date','is_featured')
    list_display_links = ('id' ,'thumbnail' , 'car_title')
    search_fields = ('car_title' , 'city' , 'state')
    list_filter = ('city','color','features','body_style')
    list_editable = ('is_featured',)
admin.site.register(car, CarAdmin)
