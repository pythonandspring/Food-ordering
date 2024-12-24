from django.contrib import admin
from .models import Comment, Feedback  # Import your models here

# admin.site.site_header = 'My Awesome Admin'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'content', 'rating', 'created_at', 'updated_at')
    search_fields = ('comment_id', 'content')
    list_filter = ('rating', 'created_at', 'updated_at')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_type', 'stars', 'comments', 'created_at')
    search_fields = ('user_type', 'comments')
    list_filter = ('stars', 'created_at')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
