from recipeservice.handlers import grpc_handlers as recipeservice_grpc_handlers

urlpatterns = []


def grpc_handlers(server):
    recipeservice_grpc_handlers(server)