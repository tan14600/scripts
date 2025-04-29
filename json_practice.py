import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(type(json.dumps(None)))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(x)   #Prints in dict
print(json.dumps(x))    #Prints out a json
print(json.dumps(x, indent=3))  #Prints out a json with formatting
print(json.dumps(x, indent=4, separators=("\ ", " = ")))    # Uses seperate formatting for JSON output
print(json.dumps(x, indent=4, sort_keys=True))