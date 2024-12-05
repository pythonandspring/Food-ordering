from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Comment(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    comment_id = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', related_name="replies", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.comment_id