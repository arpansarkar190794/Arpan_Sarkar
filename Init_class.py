class student: #Class Student
    def __init__ (self,name,age): #Method details
        self.name=name
        self.age=age
        print("The Name is {} and theage is{}".format(name,age))
student('Arpan',23)


class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"
dmp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
dmp2 = Employee("Manni", 5000)
dmp1.displayEmployee()
dmp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
        

class student: #Class Student
    def details (self,name,age): #Method details
        self.name=name
        self.age=age
        print("The Name is {} and the age is{}".format(name,age))
        print(x)
# s is an object need to be created         
    def __init__(self):
        print("Welcome to World of Python")
        x=10
