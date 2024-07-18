from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('id', 'title', 'author', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at', 'author')
    filter_horizontal = ('tags',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(PostImage)
admin.site.register(Category)
admin.site.register(Subscribe)
admin.site.register(SocialMedia)

