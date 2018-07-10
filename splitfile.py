import random
import csv

with open('token.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        rand = random.randint(1,10)
        if rand < 8:
            with open('token1.csv', 'a') as csvfile:
                filewriter1 = csv.writer(csvfile, delimiter=' ',quotechar='|')
                print(row)
                filewriter1.writerow(row)
        else:
            with open('token2.csv', 'a') as csvfile:
                filewriter2 = csv.writer(csvfile, delimiter=' ',quotechar='|')
                print(row)
                filewriter2.writerow(row)

