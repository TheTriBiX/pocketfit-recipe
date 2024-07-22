from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredients
from .serializers import IngredientsSerializer
import uuid
from .exception_handler import CustomAPIException 

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
                return Response({"error": f"{id_str} is not a valid UUIDv4"}, status=status.HTTP_400_BAD_REQUEST)

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