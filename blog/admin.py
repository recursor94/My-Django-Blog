from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):  #customize default admin for blog spots
    list_display = ('title_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title_text', 'content']
admin.site.register(Post, PostAdmin)


