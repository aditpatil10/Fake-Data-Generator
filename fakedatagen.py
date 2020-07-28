from faker import Faker
import pandas as pd
import random
import os
import csv
fake = Faker()

with open('test2.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'birthdate', 'phone', 'country', 'state', 'city', 'address', 'email', 'exam1', 'exam2', 'exam3', 'exam4', 'exam5', 'exam6']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(100):
        print(i)
        writer.writerow(
            {
                'first_name': fake.name(),
                'last_name': fake.name(),
                'birthdate': fake.date_of_birth(),
                'phone': fake.phone_number(),
                'country': fake.country(),
                'state': fake.state(),
                'city': fake.city(),
                'address': fake.street_address(),
                'email': fake.email(),
                'exam1': fake.random_int(min=60, max=80),
                'exam2': fake.random_int(min=90, max=100),
                'exam3': fake.random_int(min=40, max=70),
                'exam4': fake.random_int(min=75, max=85),
                'exam5': fake.random_int(min=30, max=50),
                'exam6': fake.random_int(min=60, max=70)
            }
        )
# with open('students.csv', 'w', newline='') as csvfile:
#     fieldnames = ['name', 'lastname', 'birthdate', 'phone no.', 'country', 'state', 'address', 'email', 'exam1', 'exam2', 'exam3', 'exam4', 'exam5', 'exam6']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for i in range(100):
#         writer.writerow(
#             {
#                 'first_name': fake.name(),
#                 'last_name': fake.name(),
#                 'birthdate': fake.date_of_birth(),
#                 'phone': fake.phone_number(),
#                 'country': fake.country(),
#                 'state': fake.state()
#                 'address': fake.street_address(),
#                 'email': fake.email(),
#                 'exam1': fake.random_int(min=60, max=80),
#                 'exam2': fake.random_int(min=90, max=100),
#                 'exam3': fake.random_int(min=40, max=70),
#                 'exam4': fake.random_int(min=75, max=85),
#                 'exam5': fake.random_int(min=30, max=50),
#                 'exam6': fake.random_int(min=60, max=70),
#
#             }
#         )

# name = []
# lastname = []
# address = []
# email = []
# exam1 = []
# exam2 = []
# exam3 = []
# exam4 = []
# exam5 = []
# exam6 = []
# fake = Faker()
# for i in range(0, 100):
#     name.append(fake.name())
#     lastname.append(fake.last_name())
#     address.append(fake.address())
#     email.append(fake.email())
#     exam1.append(fake.random_int(min=0, max=100))
#     exam2.append(n)
#     exam3.append(n)
#     exam4.append(fake.random_int(min=0, max=100))
#     exam5.append(fake.random_int(min=0, max=100))
#     exam6.append(fake.random_int(min=0, max=100))
#     print(i)
#
# person = {
#     'name':name,
#     'lastname':lastname,
#     'address':address,
#     'email':email,
#     'exam1':exam1,
#     'exam2':exam1,
#     'exam3':exam1,
#     'exam4':exam1,
#     'exam5':exam1,
#     'exam6':exam1
# }
# path ='/Users/aditpatil10/Documents/FakedataGen/student.csv'
# dataframe = pd.DataFrame(person, columns= ['name', 'lastname', 'address', 'email', 'exam1', 'exam2', 'exam3', 'exam4', 'exam5', 'exam6' ])
# dataframe.to_csv(path_or_buf=path, encoding='utf-8', index=True)
