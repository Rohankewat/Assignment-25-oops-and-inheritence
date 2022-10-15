a = 10        # Question no :- 6
b = 2

class Calculator:

    def productMethod(self):
        prt = a*b
        return prt

    def divisionMethod(self):
        div = a // b
        return div

class Calculator2(Calculator):
    pass

obj = Calculator2()

print("product is",obj.productMethod())
print("Division is",obj.divisionMethod())

