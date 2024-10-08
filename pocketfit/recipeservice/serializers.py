from django_grpc_framework import proto_serializers
from recipeservice.models import Allergy, DishCategory, UserAllergy, Ingredients, IngredientsCategory, Dish
from rest_framework import serializers
from recipe_proto import allergy_pb2
import json
from google.protobuf.json_format import MessageToDict, ParseDict, MessageToJson, Parse
import uuid

class AllergyCreateSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.AllergyCreateResponse())


class AllergyListSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.AllergyListResponse())


class AllergyRetrieveSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.AllergyRetrieveResponse())


class AllergyUpdateSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.AllergyRetrieveResponse())


class AllergyDestroySerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.AllergyDestroyResponse())


class UserAllergyListSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.ListUserAllergyResponse())


class UserAllergyCreateSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.CreateUserAllergyResponse())


class UserAllergyDestroySerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.DestroyUserAllergyResponse())


class IngredientCreateSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.IngredientCreateResponse())


class IngredientListSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.IngredientListResponse())


class IngredientRetrieveSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.IngredientRetrieveResponse())


class IngredientUpdateSerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.IngredientRetrieveResponse())


class IngredientDestroySerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.IngredientDestroyResponse())


class IngredientAddAllergySerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.IngredientAddAllergyResponse())


class IngredientDestroyAllergySerializer:
    def message_to_data(self, message):
        return MessageToDict(message, including_default_value_fields=True,
                             preserving_proto_field_name=True)

    def data_to_message(self, data):
        return Parse(json.dumps(data), allergy_pb2.IngredientDestroyAllergyResponse())
    
class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = [
            'id',
            'name',
            'translations',
            'Squirrels',
            'Fats',
            'Carbohydrates',
            'calories',
            'recipe',
            'same_ingridient',
            'image'
        ]
        read_only_fields = ['id']

    def validate_name(self, value):
        if Ingredients.objects.filter(name=value.lower()).exists():
            raise serializers.ValidationError("Ingredient with this name already exists.")
        return value.lower()

    def create(self, validated_data):
        return Ingredients.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.translations = validated_data.get('translations', instance.translations)
        instance.Squirrels = validated_data.get('Squirrels', instance.Squirrels)
        instance.Fats = validated_data.get('Fats', instance.Fats)
        instance.Carbohydrates = validated_data.get('Carbohydrates', instance.Carbohydrates)
        instance.calories = validated_data.get('calories', instance.calories)
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.same_ingridient = validated_data.get('same_ingridient', instance.same_ingridient)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
    
class AllergySerializerDRF(serializers.ModelSerializer):
    foods = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredients.objects.all(), required=False)

    class Meta:
        model = Allergy
        fields = ['id', 'name', 'translations', 'comment', 'foods']
        read_only_fields = ['id']

    def validate_id(self, value):
        if value and not isinstance(value, uuid.UUID):
            raise serializers.ValidationError("Invalid UUID format.")
        return value

    def validate_name(self, value):
        if Allergy.objects.filter(name=value.lower()).exists():
            raise serializers.ValidationError("Allergy with this name already exists.")
        return value.lower()

    def create(self, validated_data):
        foods_data = validated_data.pop('foods', [])
        allergy = Allergy.objects.create(**validated_data)
        allergy.foods.set(foods_data)
        return allergy

class UserAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAllergy
        fields = ['user_id', 'allergy_id']

    def validate_allergy_id(self, value):
        if not Allergy.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Allergy with id {value} does not exist.")
        return value
class IngredientsCategorySerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredients.objects.all())

    class Meta:
        model = IngredientsCategory
        fields = ['id', 'name', 'ingredients', 'translations']
        read_only_fields = ['id']

    def validate_name(self, value):
        if IngredientsCategory.objects.filter(name=value.lower()).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return value.lower()

    def validate_id(self, value):
        if value and not isinstance(value, uuid.UUID):
            raise serializers.ValidationError("Invalid UUID format.")
        return value

    def validate_translations(self, value):
        if value and not isinstance(value, dict):
            raise serializers.ValidationError("Translations must be a JSON object.")
        return value

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients', [])
        category = IngredientsCategory.objects.create(**validated_data)
        category.ingredients.set(ingredients)
        return category

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            instance.name = validated_data['name']
        if 'ingredients' in validated_data:
            instance.ingredients.set(validated_data['ingredients'])
        if 'translations' in validated_data:
            instance.translations = validated_data['translations']
        instance.save()
        return instance

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'recipe', 'components', 'translations', 'white_list', 'image', 'full_time', 'bizy_time']
        read_only_fields = ['id']

class DishCategorySerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Dish.objects.all())

    class Meta:
        model = DishCategory
        fields = ['id', 'name', 'dish', 'translations']
        read_only_fields = ['id']

    def validate_name(self, value):
        if DishCategory.objects.filter(name=value.lower()).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return value.lower()

    def validate_id(self, value):
        if value and not isinstance(value, uuid.UUID):
            raise serializers.ValidationError("Invalid UUID format.")
        return value

    def validate_translations(self, value):
        if value and not isinstance(value, dict):
            raise serializers.ValidationError("Translations must be a JSON object.")
        return value

    def create(self, validated_data):
        dish = validated_data.pop('dish', [])
        category = DishCategory.objects.create(**validated_data)
        category.dish.set(dish)
        return category

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            instance.name = validated_data['name']
        if 'dish' in validated_data:
            instance.dish.set(validated_data['dish'])
        if 'translations' in validated_data:
            instance.translations = validated_data['translations']
        instance.save()
        return instance