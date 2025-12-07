# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         print("THIS PERSON IS {}and age is {}".format(self.name,self.age))

# d1 = Person("Alice", 30)
# d2 = Person("Bob", 25)
# d1.walk()
# d2.walk()


# class Circle():
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return self.pi * (self.radius ** 2)   #self.pi == Cirlce.pi can be written in this way as well

#     def circumference(self):
#         return 2 * self.pi * self.radius
    


# # circle_area = Circle(5)
# # circle_circumference = Circle(7)
# # print("Area of Circle:", circle_area.area())
# # print("Circumference of Circle:", circle_circumference.circumference())


# radius = float(input("Enter the radius of the circle: "))

# circle = Circle(radius)

# print("Area of Circle:", circle.area())
# print("Circumference of Circle:", circle.circumference())

##########################################

################# INHERITANCE #################

# class Animal:
#     def __init__(self):
#         print("Animal class is created")

#     def eat(self):
#         print("This animal is eating")

#     def who_am_i(self):
#         print("I am an animal")

# # myAnimal = Animal()
# # myAnimal.eat() 
# # myAnimal.who_am_i()


# class Dog(Animal):
#     def __init__(self):
#         # Animal.__init__(self)
#         print("Dog class is created")

# myDog = Dog()
# myDog.eat()
# myDog.who_am_i()


# class tester():
#     def __init__(self, name):      ##PARENT LEVEL CLASS 
#         self.name = name       

#      def qa_role(self):
#          print("QA Role class is created here")

#     def qa_professional1(self):
#         print("QA Professional name is {}".format(self.name))

# tester1 = tester("Harini")
# tester1.qa_professional1()   


# class tester2(tester):
#     def __init__(self,name):        ##CHILD LEVEL CLASS
#         super().__init__(name)    ## BEING INHERITED FROM PARENT CLASS + USING SUPER() CAN USE THE PARENT CLASS METHODS SELF.NAME=NAME
#         # tester.__init__(self,name)
#         #print("QA Professional 2 class is created here")

# tester_2 = tester2("Balaji")
# tester_3 = tester2("Karthik")
# tester_2.qa_professional1()
# tester_3.qa_professional1()


############ POLYMORPHISM #####################

# class Dog:
#     def speak(self):
#         return "Woof!"
    
# class Cat:
#     def speak(self):
#         return "Meow!"
    
# for a in (Dog(), Cat()):
#     print(a.speak())

# arguments are passed below in polymorphism concept

class John:
    def __init__(self,name):
        self.name = name    

    def tester(self):
        return "{} is a tester".format(self.name)

class Mike:
    def __init__(self,name):
        self.name = name    

    def tester(self):
        return "{} is a tester".format(self.name)
    
class Sarah:
    def __init__(self,name):
        self.name = name    

    def tester(self):
        return "{} is a tester".format(self.name)

john = John("John Wick")
mike = Mike("Mike Tyson")
sarah = Sarah("Sarah Connor")

print(john.tester())
print(mike.tester())

for person in (john, mike,sarah):
    print(person.tester())

########################################


##### USING def __str__ instead of defining a method as john.tester() just print(john) will work ######

# class tester:
#     def __init__(self,name):
#         self.name = name    

#     def __str__(self):
#         return "{} is a tester".format(self.name)

# john = tester("John Wick")
# print(john)


####################################
