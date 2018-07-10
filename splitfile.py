import random
import csv
from tok import Tokenizer

mytok = Tokenizer()


with open('token.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        phrase = (', '.join(row))
        mytok.train(phrase)
        rand = random.randint(1,10)
        if rand < 8:
            with open('token1.csv', 'a') as csvfile:
                filewriter1 = csv.writer(csvfile, delimiter=' ',quotechar='|')
                print(mytok.seqpad(phrase, row))
                filewriter1.writerow(mytok.seqpad(phrase, row))
        else:
            with open('token2.csv', 'a') as csvfile:
                filewriter2 = csv.writer(csvfile, delimiter=' ',quotechar='|')
                print(mytok.seqpad(phrase, row))
                filewriter2.writerow(mytok.seqpad(phrase, row))
