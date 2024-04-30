from django_grpc_framework import proto_serializers
from recipeservice.models import Allergy, UserAllergy
from recipe_proto import allergy_pb2
import json
from google.protobuf.json_format import MessageToDict, ParseDict, MessageToJson, Parse


class ProtoSerializer(proto_serializers.BaseProtoSerializer, proto_serializers.Serializer):

    def message_to_data(self, message):
        """Protobuf message -> Dict of python primitive datatypes.
        """
        return MessageToDict(
            message, including_default_value_fields=True,
            preserving_proto_field_name=True
        )

    def data_to_message(self, data):
        """Protobuf message <- Dict of python primitive datatypes."""
        return ParseDict(
            data, self.Meta.proto_class(),
            ignore_unknown_fields=True
        )


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
