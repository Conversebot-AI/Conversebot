from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, default="")
    password = models.DateTimeField(auto_now_add=True)

