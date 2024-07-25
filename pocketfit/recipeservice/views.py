from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction, IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredients, Allergy, UserAllergy
from .serializers import IngredientsSerializer, AllergySerializerDRF
import uuid
from django.shortcuts import get_object_or_404
from .exception_handler import CustomAPIException, CustomAPIExceptionAllergy
import json

class IngredientsCreateView(APIView):
    def post(self, request, format=None):
        serializer = IngredientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            if 'name' in serializer.errors and 'unique' in str(serializer.errors['name'][0]):
                raise CustomAPIException({'error': 'Ingredient with this name already exists.'}, code=status.HTTP_409_CONFLICT)
            raise CustomAPIException(serializer.errors, code=status.HTTP_400_BAD_REQUEST)

class IngredientsDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            uuid_obj = uuid.UUID(str(id))
            if uuid_obj.version != 4:
                raise CustomAPIException({'error': 'Invalid UUID version.'}, code=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            raise CustomAPIException({'error': 'Invalid UUID format.'}, code=status.HTTP_400_BAD_REQUEST)

        try:
            ingredient = Ingredients.objects.get(id=uuid_obj)
        except Ingredients.DoesNotExist:
            raise CustomAPIException({'error': f'Ingredient with UUID {id} not found.'}, code=status.HTTP_404_NOT_FOUND)

        serializer = IngredientsSerializer(ingredient)
        return Response(serializer.data)
class IngredientsListView(APIView):
    def get(self, request):
        count = int(request.query_params.get('count', 10))
        offset_id = request.query_params.get('offset_id', None)

        if offset_id:
            try:
                offset_ingredient = Ingredients.objects.get(id=offset_id)
                ingredients = Ingredients.objects.filter(id__gt=offset_ingredient.id)[:count]
            except Ingredients.DoesNotExist:
                raise CustomAPIException({"error": "Invalid offset_id"}, code=status.HTTP_400_BAD_REQUEST)
        else:
            ingredients = Ingredients.objects.all()[:count]

        serializer = IngredientsSerializer(ingredients, many=True)
        return Response(serializer.data)

class IngredientsSearchView(APIView):
    def get(self, request):
        substring = request.query_params.get('substring', None)
        
        if not substring:
            return CustomAPIException({'error': 'Substring parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Проверка, что substring является строкой
        if not isinstance(substring, str):
            return CustomAPIException({'error': 'Substring must be a string'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Переводим substring в нижний регистр
        substring = substring.lower()
        
        # Поиск ингредиентов по подстроке
        ingredients = Ingredients.objects.filter(name__icontains=substring)
        serializer = IngredientsSerializer(ingredients, many=True)
        return Response(serializer.data)

class IngredientsUpdateView(APIView):
    def patch(self, request, id):
        try:
            uuid_obj = uuid.UUID(str(id))
            if uuid_obj.version != 4:
                raise CustomAPIException({"error": "Invalid UUID version"}, code=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            raise CustomAPIException({"error": "Invalid UUID format"}, code=status.HTTP_400_BAD_REQUEST)

        try:
            ingredient = Ingredients.objects.get(id=uuid_obj)
        except Ingredients.DoesNotExist:
            raise CustomAPIException({'error': f'Ingredient with UUID {id} not found.'}, code=status.HTTP_404_NOT_FOUND)

        serializer = IngredientsSerializer(ingredient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            if 'name' in serializer.errors and 'unique' in str(serializer.errors['name'][0]):
                raise CustomAPIException({"error": "Name already exists"}, code=status.HTTP_409_CONFLICT)
            raise CustomAPIException(serializer.errors, code=status.HTTP_400_BAD_REQUEST)

class IngredientsDeleteView(APIView):
    def delete(self, request, id):
        try:
            uuid_obj = uuid.UUID(str(id))
            if uuid_obj.version != 4:
                raise CustomAPIException({"error": "Invalid UUID version"}, code=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            raise CustomAPIException({"error": "Invalid UUID format"}, code=status.HTTP_400_BAD_REQUEST)

        try:
            ingredient = Ingredients.objects.get(id=uuid_obj)
        except Ingredients.DoesNotExist:
            raise CustomAPIException({'error': f'Ingredient with UUID {id} not found.'}, code=status.HTTP_404_NOT_FOUND)

        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IngredientsDeleteAll(APIView):
    def delete(self, request, format=None):
        ids = request.query_params.getlist('id')
        deleted_count = 0
        deleted_objects = []

        for id_str in ids:
            try:
                ingridient_id = uuid.UUID(id_str)
            except ValueError:
                return CustomAPIException({"error": f"{id_str} is not a valid UUIDv4"}, code=status.HTTP_400_BAD_REQUEST)

            try:
                ingridient = Ingredients.objects.get(id=ingridient_id)
                ingridient.delete()
                deleted_count += 1
                deleted_objects.append(ingridient)
            except Ingredients.DoesNotExist:
                continue

        return Response({
            "count": deleted_count,
            "deleted_objects": [ingridient.id for ingridient in deleted_objects]
        }, status=status.HTTP_200_OK)

class AllergyCreateView(APIView):
    def post(self, request, format=None):
        serializer = AllergySerializerDRF(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            if Allergy.objects.filter(name=name).exists():
                return CustomAPIException({"detail": "Allergy with this name already exists."}, code=status.HTTP_409_CONFLICT)

            foods_data = serializer.validated_data.get('foods')
            for food_id in foods_data:
                if not Ingredients.objects.filter(id=food_id).exists():
                    return CustomAPIException({"detail": f"Ingredient with id {food_id} does not exist."}, code=status.HTTP_404_NOT_FOUND)

            allergy = serializer.save()
            return Response(AllergySerializerDRF(allergy).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllergyListView(APIView):
    def get(self, request, format=None):
        count = request.query_params.get('count', 10)  # Default to 10 if not provided
        offset_id = request.query_params.get('offset_id', None)

        try:
            count = int(count)
        except ValueError:
            return CustomAPIException({"detail": "Invalid count value."}, code=status.HTTP_400_BAD_REQUEST)

        allergies = Allergy.objects.all()

        if offset_id:
            try:
                offset_id = int(offset_id)
                allergies = allergies.filter(id__gt=offset_id)
            except ValueError:
                return CustomAPIException({"detail": "Invalid offset_id value."}, code=status.HTTP_400_BAD_REQUEST)

        allergies = allergies[:count]

        serializer = AllergySerializerDRF(allergies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AllergyDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            allergy = get_object_or_404(Allergy, id=id)
        except ValueError:
            return CustomAPIException({"detail": "Invalid ID format."}, code=status.HTTP_400_BAD_REQUEST)

        serializer = AllergySerializerDRF(allergy)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AllergySearchView(APIView):
    def get(self, request, format=None):
        name = request.query_params.get('name', None)

        if not name:
            return CustomAPIException({"detail": "Name parameter is required."}, code=status.HTTP_400_BAD_REQUEST)

        allergies = Allergy.objects.filter(name__icontains=name)

        serializer = AllergySerializerDRF(allergies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AllergyUpdateView(APIView):
    def patch(self, request, id, format=None):
        try:
            allergy = get_object_or_404(Allergy, id=id)
        except ValueError:
            return CustomAPIException({"detail": "Invalid ID format."}, code=status.HTTP_400_BAD_REQUEST)

        serializer = AllergySerializerDRF(allergy, data=request.data, partial=True)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            if name and Allergy.objects.filter(name=name).exclude(id=id).exists():
                return CustomAPIException({"detail": "Allergy with this name already exists."}, code=status.HTTP_409_CONFLICT)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllergyDeleteAllView(APIView):
    def delete(self, request, format=None):
        allergy_ids = request.data.get('allergy_ids', [])

        if not allergy_ids:
            raise CustomAPIExceptionAllergy({"detail": "No allergy IDs provided."}, status.HTTP_400_BAD_REQUEST)

        try:
            allergies = Allergy.objects.filter(id__in=allergy_ids)
        except ValueError:
            raise CustomAPIExceptionAllergy({"detail": "Invalid ID format."}, status.HTTP_400_BAD_REQUEST)

        if len(allergies) != len(allergy_ids):
            missing_ids = set(allergy_ids) - set(allergies.values_list('id', flat=True))
            raise CustomAPIExceptionAllergy({"detail": f"Allergies with IDs {missing_ids} not found."}, status.HTTP_404_NOT_FOUND)

        deleted_allergies = []
        for allergy in allergies:
            deleted_allergies.append(AllergySerializerDRF(allergy).data)
            allergy.delete()

        return Response({"deleted_allergies": deleted_allergies, "count": len(deleted_allergies)}, status=status.HTTP_200_OK)
    
class AllergyDeleteView(APIView):
    def delete(self, request, id, format=None):
        try:
            allergy = get_object_or_404(Allergy, id=id)
        except ValueError:
            return CustomAPIExceptionAllergy({"detail": "Invalid ID format."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AllergySerializerDRF(allergy)
        allergy.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserAllergyView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        allergy_ids = request.data.get('allergy_ids', [])

        if not user_id:
            return CustomAPIExceptionAllergy({"detail": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Удаляем все текущие записи аллергий для данного пользователя
        UserAllergy.objects.filter(user_id=user_id).delete()

        # Создаем новые записи аллергий для данного пользователя
        for allergy_id in allergy_ids:
            try:
                allergy = Allergy.objects.get(id=allergy_id)
            except Allergy.DoesNotExist:
                return CustomAPIExceptionAllergy({"detail": f"Allergy with ID {allergy_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

            UserAllergy.objects.create(user_id=user_id, allergy_id=allergy_id)

        # Возвращаем успешный ответ
        return Response({"detail": "Allergies set successfully."}, status=status.HTTP_200_OK)