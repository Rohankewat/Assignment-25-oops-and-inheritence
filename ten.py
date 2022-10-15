class Truecaller:                # Question no :- 10

    def fetchMethod(self):
        n = int(input("Enter a number we will fetch name associated with number "))
        d1 = {8536:"aman",1785:"amar",9632:"ayush",4596:"rohan"}
        for e in d1:
            if n == e:
                print(d1[e])   

class SmartPhone:

    def newMethod(self,obj):
        obj.fetchMethod()

obj = Truecaller()
obj2 = SmartPhone()
obj2.newMethod(obj)