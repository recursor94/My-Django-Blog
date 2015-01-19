from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):  #customize default admin for blog spots
    list_display = ('title_text', 'pub_date', 'was_published_recently')
admin.site.register(Post, PostAdmin)
