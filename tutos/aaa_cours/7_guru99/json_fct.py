import json

x = {
    "name": "Ken",
    "age": 45,
    "married": True,
    "children": ("Alice", "Bob"),
    "pets": ["Dog"],
    "cars": [{"model": "Audi A1", "mpg": 15.1}, {"model": "Jeep Compass", "mpg": 18.1}],
}
# sorting result in ascending order by keys:
sorted_string = json.dumps(x, indent=4, sort_keys=False)
print(sorted_string)
print('-'*36)
sorted_string = json.dumps(x, indent=4, sort_keys=True)
print(sorted_string)
 