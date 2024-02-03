dictionary = {
    'a':1,
    'b':2,
    'x':3
}

# unordered key value pair which is immutable

print(dictionary['b'])

# dictionary keys can be an immutable datatype

dictionary = {
    123: [1,2,3],
    True: 'hello',
    '[tt]': True
}
print(dictionary[123])

# adding a new value to the same key overrides the last value

dict2 = {
    123: 10,
    123: 20
}
print(dict2[123])

user = {
    'basket': [1,2,3],
    'greet': 'hello'
}

# check if a dict has a key

print(user.get('age'))
print(user.get('age',55)) # gives a default value in case age is not present
print(user.get('age'))
print(user.get('basket'))

user2 = dict(name = 'jojo')

print(user2)

# in keyword for dictionaries

print('basket' in user)

# keys returns the keys in a list
print(user.keys())
print(user.values())
print(user.items())

print(user.clear()) #inplace function
print(user)
user2 = user.copy() # different dictionaries formed unlike '=' where just a new reference is formed
print(user2)

user = {
    'basket': [1,2,3],
    'greet': 'hello'
}
print(user.pop('basket'))
print(user.popitem()) # random item popped

print(user.update({'ages': 55}))
print(user)