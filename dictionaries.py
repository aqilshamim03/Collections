# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Aqil",
    "age": 21,
    "city": "Delhi"
}

print(person)
# Output: {'name': 'Aqil', 'age': 21, 'city': 'Delhi'}
person["email"] = "aqil@example.com"  # add new key
person["age"] = 22                     # update existing key
print(person)
# Output: {'name': 'Aqil', 'age': 22, 'city': 'Delhi', 'email': 'aqil@example.com'}
person.pop("city")   # removes 'city'
del person["email"]  # removes 'email'
print(person)
# Output: {'name': 'Aqil', 'age': 22}
