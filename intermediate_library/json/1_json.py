# converting py dict to json is called serialisation
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=3, sort_keys=True)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)