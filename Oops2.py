# class Phone:
#     def make_call(self):
#         print("make a phone call")
    
#     def play_games(self):
#         print("playing games")

# p1 = Phone()
# p1.make_call()
# p1.play_games()


# class Phone:
    
#     def set_color(self,color):
#         self.color = color
    
#     def set_cost(self,cost):
#         self.cost = cost
    
#     def show_color(self):
#         return self.color

#     def show_cost(self):
#         return self.cost
    
#     def make_call(self):
#         print("makes a phone call")
        
#     def play_games(self):
#         print("playing games")
        
        
# p2 = Phone()
# p2.set_color("blue")
# p2.set_cost(18000)
# print(p2.show_color())
# print(p2.show_cost())



# class Employee:
    
#     def __init__(self,name,age,salary,gender):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.gender = gender
        
#     def show_details(self):
#         print("Name of employee : ",self.name)
#         print("Age of employee: ",self.age)
#         print("salary of employee: ",self.salary)
#         print("gender of employye: ",self.gender)
        
# e1 = Employee("Harshad",21,25000,"Male")
# e1.show_details()


# class Vehicle:
    
#     def __init__(self,mileage,cost):
#         self.mileage = mileage
#         self.cost = cost
        
#     def show_details(self):
#         print("mileage of vehicle is ",self.mileage)
#         print("cost of vehicle is ",self.cost)
#         print("I am a vehicle")
        
# # v1 = Vehicle(250,500000)
# # v1.show_details()


# class Car(Vehicle):
    
#     def __init__(self,mileage,cost,tyres,hp):
#         super().__init__(mileage,cost)
#         self.tyres = tyres
#         self.hp = hp
        
#     def show_car_details(self):
#         print("number of tyres present in car ",self.tyres)
#         print("horse power of car is ",self.hp)
#         print("I am a car")
        
# # c1 = Car(250,600000)
# # c1.show_details()
# # c1.show_car_details()


# c2 = Car(400,800000,4,2500)
# c2.show_details()
# c2.show_car_details()



class Parent1:
    
    def assign_string1(self,str1):
        self.str1 = str1
    def show_string1(self):
        return self.str1
    
class Parent2:
    
    def assign_string2(self,str2):
        self.str2 = str2
        
    def show_string2(self):
        return self.str2
    

class child(Parent1,Parent2):
    
    def assign_string3(self,str3):
        self.str3 = str3
        
    def show_string3(self):
        return self.str3
    
    
my_child = child()
my_child.assign_string1("I am string of parent 1")
# my_child.assign_string2("I am string of parent 2")
# my_child.assign_string3("I am string of child")

my_child.show_string1()
# my_child.show_string2()
# my_child.show_string3()