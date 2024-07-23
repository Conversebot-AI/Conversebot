from django.http import HttpResponse
from rest_framework import generics
from .serializers import Bot_app
from .models import Question

class BotView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = Bot_app