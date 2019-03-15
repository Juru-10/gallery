from django.contrib import admin

from .models import Editor,Image,Location,Category

class ImageAdmin(admin.ModelAdmin):
    filter =('id','location','category')

admin.site.register(Editor)
admin.site.register(Image,ImageAdmin)
admin.site.register(Location)
admin.site.register(Category)
