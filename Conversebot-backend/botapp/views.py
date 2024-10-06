from rest_framework import generics
from .serializers import Bot_app
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

class BotView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Bot_app
    permission_classes = [AllowAny]