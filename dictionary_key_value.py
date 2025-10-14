dict = {"name": "Aqil", "age": "", "email": "","city": "", "country": "India"}
empty_keys = [key for key, value in dict.items() if not value]

if empty_keys:
    print("Below keys have empty values:")
    for key in empty_keys:
        print(key)
else:
    print("No empty values found.")