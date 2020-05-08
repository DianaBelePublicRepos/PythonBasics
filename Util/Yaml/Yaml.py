import yaml

"""
The loader in yaml imports the data into python as a dictionary

"""

with open('items.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

"""
Multiple YAML documents are read with load_all().

"""

with open('data.yaml') as f:
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:

        for k, v in doc.items():
            print(k, "->", v)


"""
The dump() method serializes a Python object into a YAML stream.

"""

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

print(yaml.dump(users))

"""
Writting Python data into a YAML file.

We write the data with the dump() method. The first parameter is the data, the second is the file object.

"""

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

with open('users.yaml', 'w') as f:
    data = yaml.dump(users, f)


"""
Sort keys with the dump's sort_keys parameter.
Read data from the items.yaml file and sorts the data by keys in the YAML output.

"""

with open('items.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    sorted = yaml.dump(data, sort_keys=True)
    print(sorted)


"""
The scan() method scans a YAML stream and produces scanning tokens.

"""

with open('items.yaml') as f:
    data = yaml.scan(f, Loader=yaml.FullLoader)

    for token in data:
        print(token)