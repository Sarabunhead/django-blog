from django.contrib import admin
from .models import post,Category
# Register your models here.

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','slug')

admin.site.register(Category)

