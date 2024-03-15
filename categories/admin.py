from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Category)

# admin k jei class ta modify kre - model admin !

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']


admin.site.register(models.Category,CategoryAdmin)