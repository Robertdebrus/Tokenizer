

class Tokenizer:

     def __init__(self):
#        print('here!')
        ad = dict()
        self.ad = ad
        num = 0
        self.num = num
        adindex = 0
        self.adindex = adindex

     def train(self, msg):
        print(msg)

        msg = msg.split(' ')
        print(msg)

        for x in msg:
            msgno = msg[self.num]
            print(msg[self.num])
            try:
                print(self.ad[msgno])
            except KeyError as ex:
                self.ad[msgno] = self.adindex
                print(self.ad[msgno])
            self.adindex += 1
            self.num += 1

mytok = Tokenizer()

mytok.train("the movie was good positive")
