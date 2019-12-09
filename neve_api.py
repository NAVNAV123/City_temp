import requests
import csv
from random import randint

# #POST request
# #TODO: connect the request to the code.
# dictToSend = {'question': 'what is the answer?'}
# resp = requests.post('http://localhost:5000/post/endpoint', json = dictToSend)
# print ('response from server: ',resp.text)
# dictFromServer = resp.json()


#read current CSV file
with open('city_temp.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are %s' % ", ".join(row))
            line_count += 1
        print('\t%s have %s temp.' % (row["city"], row["temp"]))
        line_count += 1
    print('Proccessed %s lines.' % (line_count))


rand_temp = randint(-30, 30)
city = input("Wanted city ")
if str.isdigit(city):#validation
    print("Wrong city")
else:
    print("Thank you!")
    print("the temp is %s" %rand_temp)


#write CSV file
with open('city_temp.csv', mode='w') as csv_file:
    fieldnames = ['city', 'temp']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'city': city,
                     'temp': rand_temp,
                     })
