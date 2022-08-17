from django.urls import path
from django.contrib.admin import site
from app.views import graphiql

urlpatterns = [
    path("", graphiql),
    path("admin", site.urls),
]