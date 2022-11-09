# converting py dict to json is called serialisation
import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)


# Write custom encoding function for a custom object
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJSON = UserEncoder().encode(user)
print(userJSON)


# turning json into dict
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict


user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)