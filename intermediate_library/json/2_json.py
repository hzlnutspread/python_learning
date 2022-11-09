# converting py dict to json is called serialisation
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=3, sort_keys=True)
print(personJSON)

# converting json to dict
person_new_dict = json.loads(personJSON)
print(person_new_dict)

with open('person.json', 'r') as file:
    person_new = json.load(file)
    print(person_new)