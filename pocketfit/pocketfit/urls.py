import environ
from recipeservice.handlers import grpc_handlers as recipeservice_grpc_handlers
from django.contrib import admin
from django.urls import path, include

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', include('recipeservice.urls')),
    path('', include('healthcheck.urls')),
]

if env("URL_PREFIX"):
    urlpatterns = [ path(env("URL_PREFIX"), include(urlpatterns))]
def grpc_handlers(server):
    recipeservice_grpc_handlers(server)