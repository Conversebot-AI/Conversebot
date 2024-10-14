from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def create_user(username, password):
    """
    Create a new user with the given username and password.
    """
    user = User.objects.create_user(username=username, password=password)
    return user

def get_user_by_id(user_id):
    """
    Retrieve a user by their ID.
    """
    try:
        user = User.objects.get(id=user_id)
        return user
    except ObjectDoesNotExist:
        return None

def get_user_by_username(username):
    """
    Retrieve a user by their username.
    """
    try:
        user = User.objects.get(username=username)
        return user
    except ObjectDoesNotExist:
        return None

def update_user(user_id, **kwargs):
    """
    Update the user's details like username, email, or password.
    Only fields passed in kwargs will be updated.
    """
    try:
        user = User.objects.get(id=user_id)

        # Update user fields dynamically
        for field, value in kwargs.items():
            if field == 'password':  # Handle password separately
                user.set_password(value)
            elif hasattr(user, field):
                setattr(user, field, value)
        
        user.save()
        return user
    except User.DoesNotExist:
        return None


def delete_user(user_id):
    """
    Delete a user by their ID.
    """
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return True
    except ObjectDoesNotExist:
        return False
