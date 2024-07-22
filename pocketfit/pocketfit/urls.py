from recipeservice.handlers import grpc_handlers as recipeservice_grpc_handlers
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', include('recipeservice.urls')),
    path('', include('healthcheck.urls')),
]


def grpc_handlers(server):
    recipeservice_grpc_handlers(server)