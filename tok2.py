import csv

class Tokenizer:

     def __init__(self):
#        print('here!')
        ad = dict()
        num = 0
        self.num = num
        self.ad = ad
        adindex = 0
        self.adindex = adindex

     def train(self, msg):
#        print(msg)

        msg = msg.split(',')
#        print(msg)

        for x in msg:
            msgno = msg[self.num]
            print(msg[self.num])
            try:
                print(self.ad[msgno])
            except KeyError as ex:
                self.ad[msgno] = self.num
                print(self.ad[msgno])
            self.adindex += 1
            self.num += 1
        self.num = 0
        X = self.ad[:,0:4].astype(float)
        print(X)

mytok = Tokenizer()

with open('token.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(row)
        phrase = (', '.join(row))
        print(phrase)
        mytok.train(phrase)
