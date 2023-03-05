import yaml

with open('resources/people.yml', 'r') as f: #wczytuje z yamla
    data = yaml.safe_load(f)

