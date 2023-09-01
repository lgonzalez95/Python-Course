import csv

countries_data = [
    {
        'Country': 'USA',
        'Population': 328_200_000,
        'Capital': 'Washington, D.C.',
        'Official Language(s)': 'English'
    },
    {
        'Country': 'China',
        'Population': 1_439_323_776,
        'Capital': 'Beijing',
        'Official Language(s)': 'Chinese'
    },
    {
        'Country': 'India',
        'Population': 1_380_004_385,
        'Capital': 'New Delhi',
        'Official Language(s)': 'Hindi, English'
    },
    {
        'Country': 'Brazil',
        'Population': 212_559_417,
        'Capital': 'Brasília',
        'Official Language(s)': 'Portuguese'
    },
    {
        'Country': 'Russia',
        'Population': 145_912_025,
        'Capital': 'Moscow',
        'Official Language(s)': 'Russian'
    },
    {
        'Country': 'Japan',
        'Population': 125_960_000,
        'Capital': 'Tokyo',
        'Official Language(s)': 'Japanese'
    },
    {
        'Country': 'Costa Rica',
        'Population': 5_148_668,
        'Capital': 'San José',
        'Official Language(s)': 'Spanish'
    }
]

f = open('dict-data.csv', 'w', newline='')
writer = csv.DictWriter(f, ['Country', 'Population', 'Capital', 'Official Language(s)'])
writer.writeheader()
for x in countries_data:
    writer.writerow(x)

f.close()
