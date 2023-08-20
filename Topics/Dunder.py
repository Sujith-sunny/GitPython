class person:
    
    def __init__(self, firstname, subject, city) -> None:
        self.firstname = firstname
        self.subject = subject
        self.city = city

    def __iter__(self):
        return self
    
    def __add__(self, secondname):
        self.secondname = secondname
        return self.firstname + secondname
        
    def __repr__(self) -> str:
        return 'First name is {}, Second name is {}, and he lives in {}'.format(self.firstname, self.secondname, self.city)
    
A_Person = person('Sujth', 'Human', 'Guntur')
A_Person.__add__(str('Sunny'))
print(A_Person, 'Version 1')
