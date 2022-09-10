from django.urls import path
from django.contrib.admin import site
from app.views import graphql

urlpatterns = [
    path("", graphql()),
    path("admin", site.urls),
]