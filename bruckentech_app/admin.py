from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "published", "published_at", "created_at")
	list_filter = ("published",)
	search_fields = ("title", "excerpt", "body", "author")
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ("created_at", "updated_at")
