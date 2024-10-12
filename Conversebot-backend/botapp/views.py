from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, ChatMessageSerializer
from django.contrib.auth.models import User
from .models.chat_log import ChatMessage
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ChatMessageView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all().order_by('-timestamp')  # Fetch chats, most recent first
    serializer_class = ChatMessageSerializer

    def create(self, request, *args, **kwargs):
        user_message = request.data.get('user_message')
        if not user_message:
            return Response({"error": "User message is required"}, status=status.HTTP_400_BAD_REQUEST)


        chat = ChatMessage.objects.create(user_message=user_message)
        serializer = self.get_serializer(chat)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)