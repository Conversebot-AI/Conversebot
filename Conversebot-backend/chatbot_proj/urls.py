from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("botapp/", include("botapp.urls")),
    path("admin/", admin.site.urls),
    # path("", include('Conversebot_frontend.urls'))
]