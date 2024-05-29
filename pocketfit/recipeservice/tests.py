import json

from google.protobuf.json_format import Parse, ParseDict

d = {
    "first": "a string",
    "second": True,
    "third": 123456789
}

message = ParseDict(d, Thing())
# or
message = Parse(json.dumps(d), Thing())    

print(message.first)  # "a string"
print(message.second) # True
print(message.third)  # 123456789