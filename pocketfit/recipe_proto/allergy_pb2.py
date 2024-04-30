# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recipe_proto/allergy.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1arecipe_proto/allergy.proto\x12\x07\x61llergy\"O\n\x07\x41llergy\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x0ctranslations\x18\x03 \x03(\x0b\x32\x14.allergy.Translation\"t\n\x0bTranslation\x12\x34\n\x08language\x18\x01 \x03(\x0b\x32\".allergy.Translation.LanguageEntry\x1a/\n\rLanguageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"8\n\x12\x41llergyListRequest\x12\x15\n\x08language\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_language\"P\n\x14\x41llergyCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x0ctranslations\x18\x02 \x03(\x0b\x32\x14.allergy.Translation\"H\n\x16\x41llergyRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\x08language\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_language\"9\n\x14\x41llergyUpdateRequest\x12!\n\x07\x61llergy\x18\x01 \x01(\x0b\x32\x10.allergy.Allergy\"#\n\x15\x41llergyDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"k\n\x13\x41llergyListResponse\x12!\n\x07\x61llergy\x18\x01 \x03(\x0b\x32\x10.allergy.Allergy\x12\x31\n\nerror_code\x18\x02 \x01(\x0e\x32\x1d.allergy.AllergyListErrorCode\"o\n\x15\x41llergyCreateResponse\x12!\n\x07\x61llergy\x18\x01 \x01(\x0b\x32\x10.allergy.Allergy\x12\x33\n\nerror_code\x18\x02 \x01(\x0e\x32\x1f.allergy.AllergyCreateErrorCode\"s\n\x17\x41llergyRetrieveResponse\x12!\n\x07\x61llergy\x18\x01 \x01(\x0b\x32\x10.allergy.Allergy\x12\x35\n\nerror_code\x18\x02 \x01(\x0e\x32!.allergy.AllergyRetrieveErrorCode\"o\n\x15\x41llergyUpdateResponse\x12!\n\x07\x61llergy\x18\x01 \x01(\x0b\x32\x10.allergy.Allergy\x12\x33\n\nerror_code\x18\x02 \x01(\x0e\x32\x1f.allergy.AllergyUpdateErrorCode\"N\n\x16\x41llergyDestroyResponse\x12\x34\n\nerror_code\x18\x01 \x01(\x0e\x32 .allergy.AllergyDestroyErrorCode*g\n\x14\x41llergyListErrorCode\x12\'\n#ALLERGY_LIST_ERROR_CODE_UNSPECIFIED\x10\x00\x12&\n\"ALLERGY_LIST_ERROR_CODE_VALIDATION\x10\x01*\x9a\x01\n\x16\x41llergyCreateErrorCode\x12)\n%ALLERGY_CREATE_ERROR_CODE_UNSPECIFIED\x10\x00\x12(\n$ALLERGY_CREATE_ERROR_CODE_VALIDATION\x10\x01\x12+\n\'ALLERGY_CREATE_ERROR_CODE_ALREADY_EXIST\x10\x02*\x9e\x01\n\x18\x41llergyRetrieveErrorCode\x12+\n\'ALLERGY_RETRIEVE_ERROR_CODE_UNSPECIFIED\x10\x00\x12*\n&ALLERGY_RETRIEVE_ERROR_CODE_VALIDATION\x10\x01\x12)\n%ALLERGY_RETRIEVE_ERROR_CODE_NOT_FOUND\x10\x02*\x96\x01\n\x16\x41llergyUpdateErrorCode\x12)\n%ALLERGY_UPDATE_ERROR_CODE_UNSPECIFIED\x10\x00\x12(\n$ALLERGY_UPDATE_ERROR_CODE_VALIDATION\x10\x01\x12\'\n#ALLERGY_UPDATE_ERROR_CODE_NOT_FOUND\x10\x02*\x9a\x01\n\x17\x41llergyDestroyErrorCode\x12*\n&ALLERGY_DESTROY_ERROR_CODE_UNSPECIFIED\x10\x00\x12)\n%ALLERGY_DESTROY_ERROR_CODE_VALIDATION\x10\x01\x12(\n$ALLERGY_DESTROY_ERROR_CODE_NOT_FOUND\x10\x02\x32\x8d\x03\n\x11\x41llergyController\x12\x43\n\x04List\x12\x1b.allergy.AllergyListRequest\x1a\x1c.allergy.AllergyListResponse\"\x00\x12I\n\x06\x43reate\x12\x1d.allergy.AllergyCreateRequest\x1a\x1e.allergy.AllergyCreateResponse\"\x00\x12O\n\x08Retrieve\x12\x1f.allergy.AllergyRetrieveRequest\x1a .allergy.AllergyRetrieveResponse\"\x00\x12I\n\x06Update\x12\x1d.allergy.AllergyUpdateRequest\x1a\x1e.allergy.AllergyUpdateResponse\"\x00\x12L\n\x07\x44\x65stroy\x12\x1e.allergy.AllergyDestroyRequest\x1a\x1f.allergy.AllergyDestroyResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recipe_proto.allergy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRANSLATION_LANGUAGEENTRY']._options = None
  _globals['_TRANSLATION_LANGUAGEENTRY']._serialized_options = b'8\001'
  _globals['_ALLERGYLISTERRORCODE']._serialized_start=1080
  _globals['_ALLERGYLISTERRORCODE']._serialized_end=1183
  _globals['_ALLERGYCREATEERRORCODE']._serialized_start=1186
  _globals['_ALLERGYCREATEERRORCODE']._serialized_end=1340
  _globals['_ALLERGYRETRIEVEERRORCODE']._serialized_start=1343
  _globals['_ALLERGYRETRIEVEERRORCODE']._serialized_end=1501
  _globals['_ALLERGYUPDATEERRORCODE']._serialized_start=1504
  _globals['_ALLERGYUPDATEERRORCODE']._serialized_end=1654
  _globals['_ALLERGYDESTROYERRORCODE']._serialized_start=1657
  _globals['_ALLERGYDESTROYERRORCODE']._serialized_end=1811
  _globals['_ALLERGY']._serialized_start=39
  _globals['_ALLERGY']._serialized_end=118
  _globals['_TRANSLATION']._serialized_start=120
  _globals['_TRANSLATION']._serialized_end=236
  _globals['_TRANSLATION_LANGUAGEENTRY']._serialized_start=189
  _globals['_TRANSLATION_LANGUAGEENTRY']._serialized_end=236
  _globals['_ALLERGYLISTREQUEST']._serialized_start=238
  _globals['_ALLERGYLISTREQUEST']._serialized_end=294
  _globals['_ALLERGYCREATEREQUEST']._serialized_start=296
  _globals['_ALLERGYCREATEREQUEST']._serialized_end=376
  _globals['_ALLERGYRETRIEVEREQUEST']._serialized_start=378
  _globals['_ALLERGYRETRIEVEREQUEST']._serialized_end=450
  _globals['_ALLERGYUPDATEREQUEST']._serialized_start=452
  _globals['_ALLERGYUPDATEREQUEST']._serialized_end=509
  _globals['_ALLERGYDESTROYREQUEST']._serialized_start=511
  _globals['_ALLERGYDESTROYREQUEST']._serialized_end=546
  _globals['_ALLERGYLISTRESPONSE']._serialized_start=548
  _globals['_ALLERGYLISTRESPONSE']._serialized_end=655
  _globals['_ALLERGYCREATERESPONSE']._serialized_start=657
  _globals['_ALLERGYCREATERESPONSE']._serialized_end=768
  _globals['_ALLERGYRETRIEVERESPONSE']._serialized_start=770
  _globals['_ALLERGYRETRIEVERESPONSE']._serialized_end=885
  _globals['_ALLERGYUPDATERESPONSE']._serialized_start=887
  _globals['_ALLERGYUPDATERESPONSE']._serialized_end=998
  _globals['_ALLERGYDESTROYRESPONSE']._serialized_start=1000
  _globals['_ALLERGYDESTROYRESPONSE']._serialized_end=1078
  _globals['_ALLERGYCONTROLLER']._serialized_start=1814
  _globals['_ALLERGYCONTROLLER']._serialized_end=2211
# @@protoc_insertion_point(module_scope)
