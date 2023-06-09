from django.db import models
from django.utils import timezone


class TodoItemAPI(models.Model):
    user_email = models.EmailField(max_length=50, default='User')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    deadline_at = models.DateTimeField(null=False, blank=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
