import yaml

with open('resources/people.yml', 'r') as f: #wczytuje z yamla
    data = yaml.safe_load(f)

class Person:
    def __init__(self, name, isFriend):
        self.name = name
        self.isFriend = isFriend

personlist = []
for element in data:
    name = element
    isFriend = data[element]["isFriend"]
    personlist.append(Person(name, isFriend))


