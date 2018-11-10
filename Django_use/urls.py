from django.contrib import admin
from django.urls import path
from .views import IndexHandler


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexHandler.as_view(), name='index'),
]
