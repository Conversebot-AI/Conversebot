from django.urls import path
from .views import BotView

urlpatterns = [
    path('home/', BotView.as_view())
    # path("", views.index, name="index"),

]