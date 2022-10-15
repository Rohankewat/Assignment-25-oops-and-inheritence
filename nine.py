n = int(input("Enter a number we will fetch name associated with number "))

class Truecaller:               # Question no :- 9

    def fetchMethod(self):
        d1 = {8536:"aman",1785:"amar",9632:"ayush",4596:"rohan"}
        for e in d1:
            if n == e:
                print(d1[e])   

    def entryMethod(self):
        d2 = {4536:"vansh",4512:"shreyansh",7836:"shivam",1425:"sidd"}
        print("new entry is",d2)

obj = Truecaller()
obj.fetchMethod()
obj.entryMethod()