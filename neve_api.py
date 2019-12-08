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

with open('city_temp.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are %s' % ", ".join(row))
            line_count += 1
        print('\t%s have %s temp, mode: %s.' % (row["city"], row["temp"], row["mode"]))
        line_count += 1
    print('Proccessed %s lines.' % (line_count))
