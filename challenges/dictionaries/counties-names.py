countries = {}

number_countries = int(input('Enter how many countries you want to organize: '))

for x in range(0, number_countries):
    country = input('Enter a country name: ')
    letter = country[0].upper()
    if  letter not in countries:
        countries[letter] = [country]
    else:
        countries[letter].append(country)

print(countries)