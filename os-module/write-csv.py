import csv

countries_data = [
    ('Country', 'Population', 'Capital', 'Language'),
    ('USA', 328_200_000, 'Washington, D.C.', 'English'),
    ('China', 1_439_323_776, 'Beijing', 'Chinese'),
    ('India', 1_380_004_385, 'New Delhi', 'Hindi, English'),
    ('Brazil', 212_559_417, 'Brasília', 'Portuguese'),
    ('Russia', 145_912_025, 'Moscow', 'Russian'),
    ('Japan', 125_960_000, 'Tokyo', 'Japanese'),
    ('Costa Rica', 5_148_668, 'San José', 'Spanish')
]

f = open('countries-info', 'w', newline='')
writer = csv.writer(f)
for t in countries_data:
    writer.writerow(t)
