import json
country_capitals = {}

def add_data(country, capital):
    country_capitals[country] = capital
    print(f'New record: {country} - {capital}')

def delete_data(country):
    if country in country_capitals:
        del country_capitals[country]
        print(f'Country {country} was deleted.')
        print(country_capitals)
    else:
        print(f'Country {country} not found.')

def edit_data(country, capital):
    if country in country_capitals:
        country_capitals[country] = capital
        print(f'Updated record for {country} - new capital is {capital}.')
        print(country_capitals)
    else:
        print(f'Country {country} not found.')

def find_data(country):
    if country in country_capitals:
        print(f'Capital of {country} is {country_capitals[country]}')
    else:
        print(f'Country {country} not found.')

def edit_data(country, new_capital):
    if country in country_capitals:
        country_capitals[country] = new_capital
        print(f'{country} has new capital {new_capital}')
    else:
        print(f'Country {country} not found.')

def save_data(filename):
    with open(filename, 'w') as file:
        json.dump(country_capitals, file)
    print('Data saved.')

def load_data(filename):
    with open(filename, 'r') as file:
        country_capitals = json.load(file)
    print('Data loaded successfully!')


add_data('Czechia', 'Prague')
add_data(input('Country: '), input('Capital: '))
print(country_capitals)
add_data(input('Country: '), input('Capital: '))
print(country_capitals)

delete_data(input('Delete country: '))
edit_data('Czechia', 'Opava')

find_data(input('Type country: '))

save_data('country_capitals.json')
#country_capitals.clear()
print(country_capitals)

load_data('country_capitals.json')
print(country_capitals)


