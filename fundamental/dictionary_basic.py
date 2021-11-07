import json

users = {
    'id': 1,
    'name': 'Piscki Pratama',
    'username': 'pisckitama',
    'email': 'piscki@email.com',
    'address': {
        'street': 'Good Street',
        'suite': 'Good Suite',
        'city': 'Jakarta',
        'geo': {
            'latitude': '009992',
            'langitude': '991803'
        }
    }
}

print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users['address'])
print(users['address']['street'])
print(users['address']['geo'])
print(users['address']['geo']['latitude'])
print(type(users))

# mengubah dictionary ke json
result = json.dumps(users)  # json.dumps menjadikan string
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)  # untuk menuliskan hasilnya ke file