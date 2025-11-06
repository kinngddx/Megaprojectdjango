from django.contrib import admin
from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('text', 'user__username')