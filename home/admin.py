from django.contrib import admin
from . models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category', 'slug']
    prepopulated_fields = {'slug':('category',)}

class Blog_PostAdmin(admin.ModelAdmin):
    list_display = ['id','category', 'writer', 'title', 'music']
    prepopulated_fields = {'slug':('title',)}



admin.site.register(BlogProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog_Post,Blog_PostAdmin)
admin.site.register(Comment)
admin.site.register(Visitor)
