import json
  
# Opening JSON file
with open('defects.json', 'r') as openfile:
  
    # Reading from json file
    json_object = json.load(openfile)
  
print(json_object)
print(type(json_object))
#print(json_object["Requirements"])
