import json

# use loads to convert from string to dictionary
str = '{"name": "guido", "age": 60}'
print(str)
dict = json.loads(str)
print(dict["name"])

nstr = json.dumps(dict)
print(nstr)
