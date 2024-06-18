from django.contrib import admin

from mebelevv.models import Gallery


# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    list_filter = ('title', 'date',)


admin.site.register(Gallery, GalleryAdmin)
