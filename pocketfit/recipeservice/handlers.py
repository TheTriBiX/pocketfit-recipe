from recipeservice.services import AllergyService
from recipe_proto import allergy_pb2_grpc


def grpc_handlers(server):
    allergy_pb2_grpc.add_AllergyControllerServicer_to_server(AllergyService.as_servicer(), server)