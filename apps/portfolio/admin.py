from django.contrib import admin
from apps.portfolio.models import Image, Portfolio, Comment


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "portfolio")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_by")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "image")
