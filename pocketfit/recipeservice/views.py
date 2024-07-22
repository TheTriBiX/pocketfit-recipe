from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredients
from .serializers import IngredientsSerializer
import uuid

class IngredientsCreateView(APIView):
    def post(self, request, format=None):
        serializer = IngredientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            if 'name' in serializer.errors and 'unique' in str(serializer.errors['name'][0]):
                return Response({'error': 'Ingredient with this name already exists.'}, status=status.HTTP_409_CONFLICT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientsDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            uuid.UUID(id, version=4)
        except ValueError:
            return Response({'error': 'Invalid UUID format.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ingredient = Ingredients.objects.get(id=id)
        except Ingredients.DoesNotExist:
            return Response({'error': 'Ingredient not found.'}, status=status.HTTP_404_NOT_FOUND)

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
                return Response({"error": "Invalid offset_id"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            ingredients = Ingredients.objects.all()[:count]

        serializer = IngredientsSerializer(ingredients, many=True)
        return Response(serializer.data)

class IngredientsSearchView(APIView):
    def get(self, request):
        substring = request.query_params.get('substring', '')
        if not substring:
            return Response({"error": "Substring is required"}, status=status.HTTP_400_BAD_REQUEST)

        ingredients = Ingredients.objects.filter(name__icontains=substring)
        serializer = IngredientsSerializer(ingredients, many=True)
        return Response(serializer.data)

class IngredientsUpdateView(APIView):
    def patch(self, request, id):
        try:
            uuid.UUID(id, version=4)
        except ValueError:
            return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ingredient = Ingredients.objects.get(id=id)
        except Ingredients.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = IngredientsSerializer(ingredient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            if 'name' in serializer.errors and 'unique' in str(serializer.errors['name'][0]):
                return Response({"error": "Name already exists"}, status=status.HTTP_409_CONFLICT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientsDeleteView(APIView):
    def delete(self, request, id):
        try:
            uuid.UUID(id, version=4)
        except ValueError:
            return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ingredient = Ingredients.objects.get(id=id)
        except Ingredients.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)

        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IngredientsBulkDeleteView(APIView):
    def delete(self, request):
        ids = request.query_params.getlist('id')
        deleted_ingredients = []

        for id in ids:
            try:
                uuid.UUID(id, version=4)
            except ValueError:
                return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                ingredient = Ingredients.objects.get(id=id)
                deleted_ingredients.append(ingredient)
                ingredient.delete()
            except Ingredients.DoesNotExist:
                continue

        serializer = IngredientsSerializer(deleted_ingredients, many=True)
        return Response({"count": len(deleted_ingredients), "deleted_ingredients": serializer.data})