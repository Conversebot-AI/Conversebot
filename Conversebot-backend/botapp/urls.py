from django.urls import path
from .views import UserCreateView, ChatMessageView

urlpatterns = [
    path('home/', UserCreateView.as_view())

]