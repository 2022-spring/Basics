# Chapter 6: Dictionaries (HashMap)
# element is with key-value pair, key (unique), value
# { key1: "value",
# key2: 456,
# key3: True,
# key4: ['john', 'mark'],
# key5: {'car': 'toyota', 'color': 'black'} }

alien_0 = {'color': 'green', 'points': 5}

# data structure: access(key, value), modify (key,value), delete, add
#  ... loop through the dictionaries (keys, values, keys/values)
# json
# student: ['john', 23, 456 addre st, london, uk, 89797897]
# student1: ['john', 23, 456 addre st, london, uk, 89797897]

student = {'name': ['james bond', 'agent 007'],
           'age': 23,
           'address': '456 addre st',
           'city': 'london',
           'country': 'uk',
           'tell': '89797897'}
# 'city': 'new york'}
# number of elements - len(dictName)
print('length of the dictionary, size:', len(student))

# accessing
print('accessing, name:', student['name'][1])
print('accessing, age:', student['age'] + 5)
print('accessing, country:', student['country'].upper())

customers = [
    {
        "CustomerID": "AAAAA",
        "CompanyName": "Level Up CGI",
        "ContactName": "Akmal H",
        "ContactTitle": "Instructor",
        "Address": "2906 Shell rd",
        "City": "Brooklyn",
        "Region": "NY",
        "PostalCode": "1124",
        "Country": "USA",
        "Phone": 'null',
        "Fax": 'null'
    },
    {
        "CustomerID": "AAAAB",
        "CompanyName": "My Awesome Company",
        "ContactName": 'null',
        "ContactTitle": 'null',
        "Address": 'null',
        "City": "DreamCity",
        "Region": 'null',
        "PostalCode": 'null',
        "Country": "Dreamland",
        "Phone": 'null',
        "Fax": 'null'
    }]
print(customers[1]['Country'])

# Creating empty dictionary
vacation_venues = {}
party_venues = dict()
# page 97

print("=================  04/14/2022 ==================== ")
# Agenda: Dictionaries
# CRUD - create, read, update, delete
# looping : dict(by default will be keys), dict.keys(), dict.values(), dict.items()

print("# Adding new element (key-value pairs)")
vacation_venues['city'] = 'Orlando'
vacation_venues['state'] = 'florida'
print(vacation_venues)

print("Updating the values")
vacation_venues['city'] = 'Miami'
vacation_venues['sity'] = 'tampa'
print(vacation_venues)

print("Removing Key-value pairs")
del vacation_venues['sity']
print(vacation_venues)

print('value of state: ', vacation_venues['state'])