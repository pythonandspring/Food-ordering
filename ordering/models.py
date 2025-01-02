from django.db import models

# class Ordering(models.Model):
#     ORDER_STATUS_CHOICES = [
#         ('PENDING', 'Pending'),
#         ('CONFIRMED', 'Confirmed'),
#         ('OUT_FOR_DELIVERY', 'Out for Delivery'),
#         ('DELIVERED', 'Delivered'),
#         ('CANCELLED', 'Cancelled')
#     ]
#     order_id = models.CharField(max_length=100)
#     status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='PENDING')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     order_date = models.DateTimeField(auto_now_add=True)
#     delivery_address = models.TextField()
    
#     def __str__(self):
#         return self.order_id

# class Comments(models.model):

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

class Feedback(models.Model):
    STARS_CHOICES = [(i, str(i)) for i in range(1, 6)]
    stars = models.IntegerField(choices=STARS_CHOICES)
    comments = models.TextField()
    user_type = models.CharField(max_length=20)  # 'customer', 'restaurant', or 'delivery'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_type} - {self.stars} stars"