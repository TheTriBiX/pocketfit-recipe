from recipeservice.services import AllergyService, UserAllergyService, IngredientService
from recipe_proto import allergy_pb2_grpc


def grpc_handlers(server):
    allergy_pb2_grpc.add_AllergyControllerServicer_to_server(AllergyService.as_servicer(), server)
    allergy_pb2_grpc.add_UserAllergyControllerServicer_to_server(UserAllergyService.as_servicer(), server)
    allergy_pb2_grpc.add_IngredientControllerServicer_to_server(IngredientService.as_servicer(), server)