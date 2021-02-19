from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "author", "pub_date")
    search_fields = ("title",)
    list_filter = ("pub_date", "author")
    empty_value_display = "-пусто-"
