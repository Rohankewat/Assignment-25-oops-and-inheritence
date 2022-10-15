a = 10        # Question no :- 8
b = 4

class Calculator2:

    def productMethod(self):
        prt = a*b                     
        return prt

    def divisionMethod(self):
        div = a // b             
        return div   

    
class Phoneclass:     

    def callMethod(self):
        print("calling......")

    def smsMethod(self):
        print("sms...")

class SmartPhone(Calculator2,Phoneclass):
    pass

obj = SmartPhone()
print("product is",obj.productMethod())
print("division is",obj.divisionMethod())
obj.callMethod()
obj.smsMethod()                   