from django.contrib import admin
from django.urls import include, path
from botapp.views import BotView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("botapp/", include("botapp.urls")),
    path("admin/", admin.site.urls),
    path("user/register/", BotView.as_view(), name="register"),
    path("token/",TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh",TokenRefreshView.as_view(), name="refresh"),
    path("auth/", include("rest_framework.urls")),
]