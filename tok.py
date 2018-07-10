import csv

class Tokenizer:

    def __init__(self):
        self.ad = dict()
        self.ad['S'] = 1
        self.ad['E'] = 2
        self.adindex = 3

    def train(self, msg):
        msg = msg.lower()
        msg = msg.split(',')
        msg = msg[:-1]
        for i,x in enumerate(msg):
            msgword = msg[i]
            try:
                self.ad[msgword]
            except KeyError as ex:
                self.ad[msgword] = self.adindex
                self.adindex += 1

    def printdat(self):
        for w in self.ad:
            print(w, self.ad[w])

    def seqpad(self, sent, n):
        sent = sent.lower()
        sent = sent.split(',')
        sent = sent[:-1]
        senttoken = [1]
        for i,x in enumerate(sent):
            sentword = sent[i]
            num = self.ad[sentword]
            senttoken.append(num)
        senttoken.append(2)
        while len(senttoken) < 10:
            senttoken.append(0)
        return(senttoken)

mytok = Tokenizer()

with open('token.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        phrase = (', '.join(row))
        mytok.train(phrase)
        mytok.seqpad(phrase, row)
    mytok.printdat()
