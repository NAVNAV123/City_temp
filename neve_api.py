import requests
import csv
from random import randint

# rand_temp = randint(-30, 30)
# city = input("Wanted city ")
# if str.isdigit(city):
#     print("Wrong city")
# else:
#     print("Thank you!")
#     print("the temp is %s" %rand_temp)

with open('city_temp.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('city_temp.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)