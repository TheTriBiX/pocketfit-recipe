import grpc
from google.protobuf import empty_pb2
from recipe_proto import allergy_pb2
from django_grpc_framework.services import Service
from recipeservice.models import Allergy, UserAllergy
from recipeservice.serializers import *
from django.db import IntegrityError


def find_translation(target, translations):
    for translate in translations:
        if target in translate['language']:
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
        elif 'language' in data:
            response['allergy'] = [{'id': allergy.pk,
                                    'name': allergy.name,
                                    'translations': find_translation(data['language'], allergy.translations)}
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
        print(response)
        return serializer.data_to_message(response)
