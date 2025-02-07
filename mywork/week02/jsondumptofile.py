import json

data = {
    "name" : "joe",
    "age" : 21,
    "student" : True
    }
# print(data)

# dumps into dict objects
file = open("simple.json", 'w')
json.dump(data, file, indent=4)
#dumps = dump string
jsonString = json.dumps(data)
print(jsonString)