import json

data0 = {"语文": "95.0", "数学": "99.0", "外语": "96.0"}
data1 = {"yuwen": "95.0", "shuxue": "99.0", "waiyu": "96.0"}
print(type(data0))
json_data = json.dumps(data1, ensure_ascii=False)
print(type(json_data), json_data)

print(json_data.count("waiyu"))
print(json_data.upper())
print(json_data.capitalize())

