from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_notifications'
    )
    message = models.TextField(default="New notification")
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}..."

    def mark_as_read(self):
        """Mark this specific notification as read"""
        self.is_read = True
        self.save()