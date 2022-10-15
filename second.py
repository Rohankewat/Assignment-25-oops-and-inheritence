class Profile:        # Question no :- 2

    def __init__(self):
        self.name = "rohan"
        self.email = "rohan2251@gmail.com"
        self.age = 24

    def set_name(self,name):
        self.name = name
        
    def get_name(self):
        return self.name

    def set_email(self,email):
        self.email = email

    def get_email(self):
        return self.email 
    
    def set_age(self,age):
        self.age = age

    def get_age(self):
        return self.age

det1 = Profile()
det1.set_name("aman")
det1.set_email("aman2258@gmail.com")
det1.set_age(22)

print(det1.get_name())
print(det1.get_email())    
print(det1.get_age())  