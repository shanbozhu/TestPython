import json

json_str = "{\"1\": \"2\", \"2\": \"3\"}"

json_dict = json.loads(json_str)
print(json_dict)
json_str = json.dumps(json_dict)
print(json_str)
pass