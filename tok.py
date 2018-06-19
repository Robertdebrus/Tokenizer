class Tokenizer:

     def __init__(self):
#        print('here!')
        ad = dict()
        self.ad = ad


     def train(self, msg):
        print(msg)

        msg.spilt(' ')
        print(msg)

        try:
            print(self.ad[msgno])
        except KeyError as ex:
            self.ad[msgno] = adindex
            adindex +=1
            print(self.ad[msgno])

        print('got here!')


mytok = Tokenizer()

mytok.train("the,movie,was,good,positive")
