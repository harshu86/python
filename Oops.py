"""
class Remote():
    pass

class Player():
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass
    
remote1 = Remote()
player1 = Player()

if (remote1.isLeftPressed()):
    player1.moveLeft()
"""

##
# class Railway():
#     formType = "Raiwayform"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.Train}")

# harshadApplicaton = Railway()
# harshadApplicaton.name = "Harshad"
# harshadApplicaton.Train = "Rajdhani Express"
# harshadApplicaton.printData()

"""

class Employee():
    company = "Google"
    Salary = 100

harshad = Employee()
sharad = Employee()
print(harshad.company)
print(sharad.company)
Employee.company = "YouTube"
print(harshad.company)
print(sharad.company)

# Creating instance attributes salary for both the object
# harshad.Salary = 200
# sharad.Salary = 250

print(harshad.Salary)
print(sharad.Salary)

"""
# @staticmethod
# class Employee:
#     Company = "Google"
#     def getSalary(self,signature):
#         print(f"Salary is {self.salary} \n{signature}")

#     @staticmethod
#     def greet():        #(self)
#         print("Good Morning,Sir")



# harshad = Employee()
# harshad.salary = 100000
# # Employee.getSalary(harshad)
# harshad.getSalary("Thanks!")
# harshad.greet()

"""
#__init__ fuction

class Employee:
    company = "Google"

    def __init__(self,name,salary,unit):
        self.name = name
        self.salary = salary
        self.unit = unit
        print("Employee is created")

    def getDeatails(self):
        print(f"Employee name is {self.name} and his salary is {self.salary} and his work form this company {self.unit}")
    
harshad = Employee("harshad",10000,"YouTube")
harshad.getDeatails()

"""

"""
#1
class Programmer():
    company = "Microsoft"
    
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of {self.company} programmer is {self.name} and the product is {self.product}")
    
harshad = Programmer("Harshad" , "insta")
harshad.getInfo()


#2
class  Calculator:
    def __init__(self,num):
        self.number  = num

    def square(self):
        print(f"the number is {self.number} and square of the number is {self.number**2}")
    
    def squareroot(self):
        print(f"the number is {self.number} and squareroot of the number is {self.number**0.5}")
    
    def cube(self):
        print(f"the number is {self.number} and cube of the number is {self.number**3}")
        

a = Calculator(4)
a.square()
a.squareroot()
a.cube()


#3
class Sample:
    a = "harshad"

obj = Sample()
obj.a = "sharad"
                        #It doesnt change a class attributes
# Sample.a = "kamlesh"    change the class attributes
print(Sample.a)
print(obj.a)


#4
class  Calculator:
    def __init__(self,num):
        self.number  = num

    def square(self):
        print(f"the number is {self.number} and square of the number is {self.number**2}")
    
    def squareroot(self):
        print(f"the number is {self.number} and squareroot of the number is {self.number**0.5}")
    
    def cube(self):
        print(f"the number is {self.number} and cube of the number is {self.number**3}")
    
    @staticmethod
    def greet():
        print("*******Hello friend now use me for best results!... my name is calculator*******")

a = Calculator(4)
a.greet()
a.square()
a.squareroot()
a.cube()


#5 
class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("*************")
        print(f"The Train name is {self.name}")
        print(f"The seats available in this Train are :{self.seats}")
        print("*************")

    def fareInfo(self):
        print(f"The ticket cost is {self.fare}")

    def bookTickets(self):
        if(self.seats > 0):
            print("Your Tickes has been booked")
            self.seats = self.seats - 1 
        else:
            print("No seats available in this Train")

Intercity = Train("Intercity Express: 14015",90,300)
Intercity.getStatus()
Intercity.fareInfo()        

Intercity.bookTickets()     #Ticket 1
Intercity.bookTickets()        #Ticket 2
Intercity.bookTickets()         #Ticket 3

Intercity.getStatus()


#6

class Sample:
    def __init__(slf,name):    #instead o self we are using any parameter but progrmmer dont understand so write self
        slf.name = name
    
obj = Sample("Harshad")
print(obj.name)

"""


# #Inheritence
# class Employee:
#     company = "Googgle"
    
#     def showDetails(self):
#         print("This is an Employee")

# class Programmer(Employee):
#     langauge = "Python"
        
#     def getLangauge(self):
#         print(f"The langauge is {self.langauge}")

#     # def showDetails(self):                   Over write   
#     #     print("This is an programmer")

# h = Employee()
# h.showDetails()
# p = Programmer()
# p.showDetails()
# h.showDetails()
# print(p.company)



# #multiple Inheritence
# class Employee:
#     company = "Visa"
#     eCode = 120

# class Freelancer:
#     company = "Fiverr"
#     level = 0

#     def upgardeLevel(self):
#         self.level = self.level + 1

# class Programmer(Employee,Freelancer):      #priorty
#     name = "Harshad"


# p = Programmer()
# p.upgardeLevel()
# print(p.level)
# print(p.company)
# print(p.company)



# #multilevel
# class Person:
#     country = "India"

#     def takeBreath(self):
#         print("I am breathing....")

# class Employee(Person):
#     company = "Honda"

#     def getSalary(self):
#         print(f"salary is {self.salary}")

#     def takeBreath(self):
#                                          #super().takeBreath()
#         print("I am an Employee so I am luckily breathing....")

# class Programmer(Employee):
#     company = "Fiverr" 

#     def getSalary(self):
#         print("NO salary to programmer")     

# p = Person()
# p.takeBreath()
# e = Employee()
# e.takeBreath()
# pr = Programmer()
# print(pr.company)
# print(e.company)   
# print(p.country)
# print(pr.country)       
# print(e.country)
# pr.takeBreath()
# pr.getSalary()


# class Employee:
#     company = "Camel"
#     salary = 100
#     location = "Delhi"

#     # def changeSalary(self, sal):
#     #     self.salary = sal
#     #        # __class__
    
#     @classmethod       
#     def changeSalary(cls, sal):
#         cls.salary = sal
        


# e = Employee()
# print(e.salary)
# e.changeSalary(456)
# print(e.salary)
# print(Employee.salary)
# print(Employee.company)



# class Employee:
#     company = "Bharat Gas"
#     salary = 5600
#     salarybonus = 500
#     # totalsalary = 6100

#     @property
#     def totalSalary(self):
#         return self.salary + self.salarybonus
    
#     @totalSalary.setter
#     def totalSalary(self,val):
#         self.salarybonus = val - self.salary

# e = Employee()
# print(e.totalSalary)
# e.totalSalary = 5800
# print(e.salary)
# print(e.salarybonus) 



# class Number:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self,num2):
#         print("Lets add")
#         return self.num + num2.num

#     def __mul__(self,num2):
#         print("Lets multiply")
#         return self.num * num2.num
    
#     def __truediv__(self,num2):
#         print("Lets divide")
#         return self.num / num2.num


# n1 = Number(4)
# n2 = Number(6)

# sum = n1 + n2
# mul = n1 * n2
# print(sum)
# print(mul)
# div = n1 / n2
# print(div)



# class Number:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self,num2):
#         print("Lets add")
#         return self.num + num2.num

#     def __str__(self):
#         return f"decimal number: {self.num}"

#     def __len__(self):
#         return 1

# n = Number(9)
# print(n)
# print(len(n))

"""

#1
class C2dVec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dvec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(1,3)
v3d = C3dvec(1,9,7)
print(v2d)
print(v3d)



#2
class Animals:
    animalType = "Mammal"

class Pet:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("bow bow")

d = Dog()
d.bark()



#3
class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)



#4
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self,c):
        return Complex(self.real + c.real , self.imaginary + c.imaginary)

    def __mul__(self,c):
        mulReal = self.real * c.real - self.imaginary * c.imaginary
        mulImg = self.real * c.imaginary + self.imaginary * c.real
        return Complex(mulReal, mulImg)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(1,4)
c2 = Complex(8,5)
print(c1+c2)
print(c1 * c2)



#5
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self,vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return Vector(newlist)

    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += (self.vec[i] * vec2.vec[i])
        return sum

v1 = Vector([1, 4, 6])
v2 = Vector([1,5,3])
print(v1)
print(v1+v2)
print(v1*v2)



#6
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1 = Vector([1, 4, 6])
v2 = Vector([1,5,3])
print(v1)



#7
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self,vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return Vector(newlist)

    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += (self.vec[i] * vec2.vec[i])
        return sum

    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6])
v2 = Vector([1,5,3,5,9,5])
print(v1)
print(len(v1))
print(len(v2))

"""
