from django.db import models
from .users import User

class ChatMessage(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.user_message} | Bot: {self.bot_response}"