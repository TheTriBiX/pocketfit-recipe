import grpc
from google.protobuf import empty_pb2
from recipe_proto import allergy_pb2
from django_grpc_framework.services import Service
from recipeservice.models import Allergy, UserAllergy, Ingredients, IngredientsAllergy
from recipeservice.serializers import *
from django.db import IntegrityError


def find_translation(target, translations):
    for translate in translations:
        if target in translate['languages']:
            return [translate]


class AllergyService(Service):

    def Create(self, request, context):
        serializer = AllergyCreateSerializer()
        data = serializer.message_to_data(message=request)
        response = dict()
        response['error_code'] = 0
        if not data['name'] or not data['translations']:
            response['error_code'] = 1
            return serializer.data_to_message(data)
        try:
            new_obj = Allergy(name=data['name'], translations=data['translations'])
            new_obj.save()
            response['allergy'] = {'id': new_obj.pk,
                                   'name': new_obj.name,
                                   'translations': new_obj.translations}
        except IntegrityError:
            existed_obj = Allergy.objects.get(name=data['name'])
            response['allergy'] = {'id': existed_obj.pk,
                                   'name': existed_obj.name,
                                   'translations': existed_obj.translations}
            response['error_code'] = 2

        return serializer.data_to_message(response)

    def List(self, request, context):
        serializer = AllergyListSerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if not data:
            response['allergy'] = [{'id': allergy.pk,
                                    'name': allergy.name,
                                    'translations': allergy.translations} for allergy in Allergy.objects.all()]
        elif 'languages' in data:
            response['allergy'] = [{'id': allergy.pk,
                                    'name': allergy.name,
                                    'translations': find_translation(data['languages'], allergy.translations)}
                                   for allergy in Allergy.objects.all()]
        else:
            response['error_code'] = 1
        return serializer.data_to_message(response)

    def Retrieve(self, request, context):
        serializer = AllergyRetrieveSerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if data['id'] != 0:
            try:
                allergy = Allergy.objects.get(pk=data['id'])
                translation = find_translation(data['language'],
                                               allergy.translations) if 'language' in data else allergy.translations
                response['allergy'] = {'id': allergy.pk,
                                       'name': allergy.name,
                                       'translations': translation}
            except Allergy.DoesNotExist:
                response['error_code'] = 2
        else:
            response['error_code'] = 1
        return serializer.data_to_message(response)

    def Update(self, request, context):
        serializer = AllergyUpdateSerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if data and data['allergy']['id'] != 0:
            try:
                allergy = Allergy.objects.get(pk=data['allergy']['id'])
                allergy.name = data['allergy']['name']
                allergy.translations = data['allergy']['translations']
                response['allergy'] = {'id': allergy.pk,
                                       'name': allergy.name,
                                       'translations': allergy.translations}
            except Allergy.DoesNotExist:
                response['error_code'] = 2
        else:
            response['allergy'] = None
            response['error_code'] = 1
        return serializer.data_to_message(response)

    def Destroy(self, request, context):
        serializer = AllergyDestroySerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if data['id'] == 0:
            response['error_code'] = 1
        else:
            try:
                Allergy.objects.get(id=data['id']).delete()
            except Allergy.DoesNotExist:
                response['error_code'] = 2
        return serializer.data_to_message(response)


class UserAllergyService(Service):
    def List(self, request, context):
        serializer = UserAllergyListSerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if not data['user_id']:
            return serializer.data_to_message(response)
        allergies = UserAllergy.objects.filter(user_id=data['user_id'])
        response['user_id'] = data['user_id']
        response['allergies_id'] = [i.pk for i in allergies]
        return serializer.data_to_message(response)

    def Create(self, request, context):
        serializer = UserAllergyCreateSerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0, 'user_id': data['user_id'], 'allergy_id': data['allergy_id']}
        if not (data['user_id'] and data['allergy_id']):
            response['error_code'] = 1
            return serializer.data_to_message(response)
        try:
            allergy_id = Allergy.objects.get(pk=data['allergy_id']).id
            new_obj = UserAllergy(allergy_id=allergy_id, user_id=data['user_id']).save()
        except Allergy.DoesNotExist:
            response['error_code'] = 2
        except IntegrityError:
            allergy_id = Allergy.objects.get(pk=data['allergy_id']).id
            response['error_code'] = 3
        return serializer.data_to_message(response)

    def Destroy(self, request, context):
        serializer = UserAllergyDestroySerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if not (data['user_id'] and data['allergy_id']):
            response['error_code'] = 1
            return serializer.data_to_message(response)
        try:
            obj = UserAllergy.objects.get(user_id=data['user_id'], allergy_id=data['allergy_id']).delete()
        except UserAllergy.DoesNotExist:
            response['error_code'] = 2
        return serializer.data_to_message(response)


class IngredientService(Service):
    def Create(self, request, context):
        serializer = IngredientCreateSerializer()
        data = serializer.message_to_data(message=request)
        response = {'error_code': 0}
        if not data['name'] or not data['translations']:
            response['error_code'] = 1
            return serializer.data_to_message(data)
        try:
            new_obj = Ingredients(name=data['name'], translations=data['translations'])
            new_obj.save()
            response['ingredient'] = {'id': new_obj.pk,
                                      'name': new_obj.name,
                                      'translations': new_obj.translations}
        except IntegrityError:
            existed_obj = Ingredients.objects.get(name=data['name'])
            response['ingredient'] = {'id': existed_obj.pk,
                                      'name': existed_obj.name,
                                      'translations': existed_obj.translations}
            response['error_code'] = 2

        return serializer.data_to_message(response)

    def List(self, request, context):
        serializer = IngredientListSerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if not data:
            response['ingredients'] = [{'id': ingredient.pk,
                                        'name': ingredient.name,
                                        'translations': ingredient.translations} for ingredient in
                                       Ingredients.objects.all()]
        elif 'language' in data:
            response['ingredients'] = [{'id': ingredient.pk,
                                        'name': ingredient.name,
                                        'translations': find_translation(data['language'], ingredient.translations)}
                                       for ingredient in Ingredients.objects.all()]
        else:
            response['error_code'] = 1
        return serializer.data_to_message(response)

    def Retrieve(self, request, context):
        serializer = IngredientRetrieveSerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if data['ingredient_id'] != 0:
            try:
                ingredient = Ingredients.objects.get(pk=data['ingredient_id'])
                translation = find_translation(data['language'],
                                               ingredient.translations) if data['language'] else ingredient.translations
                response['ingredient'] = {'id': ingredient.pk,
                                          'name': ingredient.name,
                                          'translations': translation}
            except Ingredients.DoesNotExist:
                response['error_code'] = 2
        else:
            response['error_code'] = 1
        return serializer.data_to_message(response)

    def Update(self, request, context):
        serializer = IngredientUpdateSerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if data and data['ingredient']['id'] != 0:
            try:
                ingredient = Ingredients.objects.get(pk=data['ingredient']['id'])
                ingredient.name = data['ingredient']['name']
                ingredient.translations = data['ingredient']['translations']
                response['ingredient'] = {'id': ingredient.pk,
                                          'name': ingredient.name,
                                          'translations': ingredient.translations}
            except Ingredients.DoesNotExist:
                response['error_code'] = 2
        else:
            response['ingredient'] = None
            response['error_code'] = 1
        return serializer.data_to_message(response)

    def Destroy(self, request, context):
        serializer = IngredientDestroySerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0}
        if not data['ingredient_id']:
            response['error_code'] = 1
        else:
            try:
                Ingredients.objects.get(id=data['ingredient_id']).delete()
            except Ingredients.DoesNotExist:
                response['error_code'] = 2
        return serializer.data_to_message(response)

    def AddAllergy(self, request, context):
        serializer = IngredientAddAllergySerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0, 'allergy_id': data['allergy_id'], 'ingredient_id': data['ingredient_id']}
        if not (data['allergy_id'] and data['ingredient_id']):
            response['error_code'] = 1
            return serializer.data_to_message(response)
        try:
            ingredient = Ingredients.objects.get(pk=data['ingredient_id'])
            allergy = Allergy.objects.get(pk=data['allergy_id'])
            new_obj = IngredientsAllergy(allergy_id=allergy.pk, ingredient_id=ingredient.pk).save()
        except Allergy.DoesNotExist:
            response['error_code'] = 2
        except Ingredients.DoesNotExist:
            response['error_code'] = 3
        except IntegrityError:
            response['error_code'] = 4
        return serializer.data_to_message(response)

    def DestroyAllergy(self, request, context):
        serializer = IngredientDestroyAllergySerializer()
        data = serializer.message_to_data(request)
        response = {'error_code': 0, 'allergy_id': data['allergy_id'], 'ingredient_id': data['ingredient_id']}
        if not (data['allergy_id'] and data['ingredient_id']):
            response['error_code'] = 1
            return serializer.data_to_message(response)
        try:
            IngredientsAllergy.objects.get(allergy_id=data['allergy_id'], ingredient_id=data['ingredient_id']).delete()
        except IngredientsAllergy.DoesNotExist:
            response['error_code'] = 2
        return serializer.data_to_message(response)
