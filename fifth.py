class Calculator:           # Question no :- 5

    def __init__(self,n1):
        self.n1 = n1            

    def __add__(self,other):
        sum_total = self.n1 + other.n1
        calc3 = Calculator(sum_total)
        return calc3

    def __sub__(self,other):
        sub_total = self.n1-other.n1
        calc4 = Calculator(sub_total)
        return calc4
    
calc1 = Calculator(25) 
calc2 = Calculator(5)

calc4 = calc1-calc2
calc3 = calc1 + calc2      # Calculator.__add__(calc1,calc2)
                           # calc1.__add__(calc2)
print("Addition is",calc3.n1)
print("Subtraction is",calc4.n1)     