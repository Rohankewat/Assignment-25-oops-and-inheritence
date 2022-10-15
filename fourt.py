class Profile:        # Question no :- 4
    cls_variable = 25
     
    @classmethod              
    def classmethod(cls):
        return cls.cls_variable

new1 = Profile()

print(Profile.classmethod())    