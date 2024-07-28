from django_grpc_framework import proto_serializers
from recipeservice.models import Allergy, UserAllergy, Ingredients, IngredientsCategory
from rest_framework import serializers
from recipe_proto import allergy_pb2
import json
from google.protobuf.json_format import MessageToDict, ParseDict, MessageToJson, Parse


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
        fields = '__all__'

class AllergySerializerDRF(serializers.ModelSerializer):
    foods = serializers.PrimaryKeyRelatedField(queryset=Ingredients.objects.all(), many=True)

    class Meta:
        model = Allergy
        fields = ['id', 'name', 'translations', 'comment', 'foods']

    def create(self, validated_data):
        foods_data = validated_data.pop('foods')
        allergy = Allergy.objects.create(**validated_data)
        allergy.foods.set(foods_data)
        return allergy
    def update(self, instance, validated_data):
        foods_data = validated_data.pop('foods', None)
        instance = super().update(instance, validated_data)
        if foods_data is not None:
            instance.foods.set(foods_data)
        return instance

class UserAllergySerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    allergy_ids = serializers.ListField(child=serializers.IntegerField())

class IngredientsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsCategory
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        category = IngredientsCategory.objects.create(**validated_data)
        for ingredient in ingredients_data:
            category.ingredients.add(ingredient)
        return category