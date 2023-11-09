# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# python 3.7 onwards dictionaries became ordered and before it, it was unordered

info = {'name':'sam', 'age':'19', 'eligible':True}
# to print the dictionary 
print(info)

# accessing dictionary items----
# accessing dictionary single items:two methods------ sq.brackets and get 
print(info['name'])
print(info.get('name'))

# the difference is sq.bracket method throws error(keyError) if keyword is not present in the dictionary but the get method gives output as none if the keyword is not present

# to access all keys/values 
print(info.keys())
print(info.values())


# it itrate all the keys/values one by one
for key in info.keys():
    print(key)         # key dega
    print(info[key])      # value dega



for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

# ṣyntax-----dictionary ka naaam[key]

# Accessing key-value pairs: can be done by following way
print(info.items())
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")












