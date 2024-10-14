from ..models.chat_log import ChatMessage
from django.core.exceptions import ObjectDoesNotExist

def get_all_chat_messages():
    """
    Retrieve all chat messages ordered by timestamp.
    """
    return ChatMessage.objects.all().order_by('-timestamp')

def get_chat_message_by_id(chat_id):
    """
    Retrieve a single chat message by its ID.
    """
    try:
        return ChatMessage.objects.get(id=chat_id)
    except ObjectDoesNotExist:
        return None

def create_chat_message(user_message):
    """
    Create a new chat message.
    """
    return ChatMessage.objects.create(user_message=user_message)

def update_chat_message(chat_id, new_message):
    """
    Update an existing chat message.
    """
    try:
        chat = ChatMessage.objects.get(id=chat_id)
        if chat:
            chat.user_message = new_message
            chat.save()
        return chat
    except ObjectDoesNotExist:
        return None

def delete_chat_message(chat_id):
    """
    Delete a chat message by its ID.
    """
    try:
        chat = ChatMessage.objects.get(id=chat_id)
        chat.delete()
        return True
    except ObjectDoesNotExist:
        return False
