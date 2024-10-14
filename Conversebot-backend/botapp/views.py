from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ChatMessageSerializer, UserSerializer
from .crud import crud_chat_log, crud_user

class UserCreateView(generics.CreateAPIView):
    """
    API view to handle user registration.
    """
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = crud_user.create_user(username=username, password=password)
        if user:
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Unable to create user."}, status=status.HTTP_400_BAD_REQUEST)

class ChatMessageView(generics.ListCreateAPIView):
    """
    API view for listing and creating chat messages.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ChatMessageSerializer

    def get(self, request, *args, **kwargs):
        messages = crud_chat_log.get_all_chat_messages()
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_message = request.data.get('user_message')
        if not user_message:
            return Response({"error": "User message is required"}, status=status.HTTP_400_BAD_REQUEST)

        chat = crud_chat_log.create_chat_message(user_message)
        serializer = self.get_serializer(chat)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ChatMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to handle retrieving, updating, and deleting individual chat messages.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ChatMessageSerializer

    def get(self, request, *args, **kwargs):
        chat_id = self.kwargs.get('pk')
        chat = crud_chat_log.get_chat_message_by_id(chat_id)
        if chat:
            serializer = self.get_serializer(chat)
            return Response(serializer.data)
        return Response({"error": "Chat message not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        chat_id = kwargs.get('pk')
        user_message = request.data.get('user_message')

        chat = crud_chat_log.update_chat_message(chat_id, user_message)
        if chat:
            serializer = self.get_serializer(chat)
            return Response(serializer.data)
        return Response({"error": "Chat message not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        chat_id = kwargs.get('pk')
        if crud_chat_log.delete_chat_message(chat_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Chat message not found."}, status=status.HTTP_404_NOT_FOUND)
