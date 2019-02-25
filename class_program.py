class student:
    def details (self,name,age,dob):
        self.name=name
        self.age=age
        self.dob=dob
        print("The Name is {} and theage is{} dob: {}".format(name,age,dob))
d=student
d.details('Arpan',23,19/07/1995)