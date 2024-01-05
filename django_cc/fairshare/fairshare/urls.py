from django.contrib import admin
from django.urls import path, include
from fairshare_backend.views import get_users
from fairshare_backend.views import new_user

urlpatterns = [
    path('', include("fairshare_backend.urls")),
    path('admin/', admin.site.urls),
    path('get_users/', get_users),
    path('new_user/', new_user),
]
