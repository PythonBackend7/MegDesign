from django.contrib import admin
from .models import *


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Subscriber)
admin.site.register(Social_Media)
admin.site.register(Extra_Images)
