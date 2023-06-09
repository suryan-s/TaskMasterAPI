from rest_framework import serializers
from .models import TodoItemAPI


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItemAPI
        exclude = ['user_email', 'created_at', 'is_completed']
