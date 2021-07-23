# from django.contrib import admin
# from .models import Tag, Image


# # Register your models here
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ['id','name']


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['id','tag','address','description']


from django.contrib import admin

# Register your models here.

from .models import Tag, PhotoImage

admin.site.register(Tag)
admin.site.register(PhotoImage)