# Class - Blueprint for creating objects
# Object - Instance of a class
# Attributes - Variables that belong to an object
# Methods - Functions that belong to an object



# Class & Object

class Student:

    # Class attribute
    SSC_Batch = 2026
    num_of_student = 0 # The number of students is depend on the number of object with new student details

    # Constructor
    def __init__(self,name,group):

        # Instance attributes
        self.name = name
        self.group = group
        Student.num_of_student += 1 # Class attribute

    def display(self):
        return f"My name is {self.name} and I'm a student of {self.group} group."

    def display_(self):
        return f"I'm a examer of SSC Batch {Student.SSC_Batch}." # I can use "Student.SSC_Batch" because it's a Class attribute but "self.SSC_Batch" also allowed.
     
    def display__(self,editor,code = "Python"):
        return f"I love to code in {code} on {editor}."

Object = Student("Shamim Ahmed Nahid","Science")
print(Object.display()) # My name is Shamim Ahmed Nahid and I'm a student of Science group.
print(Object.display_()) # I'm a examer of SSC Batch 2026.
print(Object.display__("VS Code")) # I love to code in Python on VS Code.
print(Student.num_of_student) # 1



# Inheritance

# Parent class (Base class)
class school:

    def __init__(self,Class,Section,Name):
        self.Class = Class
        self.Section = Section
        self.Name = Name
    
    def name(self):
        return f"My name is {self.Name}. I'm a student of class {self.Class} in section {self.Section}."


# Child class (Derived class)
class Ten(school):

    def name(self):
        return f"Hi I'm {self.Name}" # Overriding parent method.
    
    def roll(self): # New method specific to Ten
        return "My roll is 45"

Object = Ten(10,"A","Shamim Ahmed Nahid")
print(Object.name()) # Hi I'm Shamim Ahmed Nahid
print(Object.roll()) # My roll is 45


# Child class (Derived class)
class Other(school):
    pass

object = Other(10,"A","Shamim Ahmed Nahid")
print(object.name()) # My name is Shamim Ahmed Nahid. I'm a student of class 10 in section A.



# Multilevel Inheritance (Grandparent → Parent → Child)

# Grandparent class
class Grandparent:
    
    def __init__(self,name):
        self.name = name
    
    def display(self):
        return f"This is {self.name} Class"

# Parent class
class Parent(Grandparent):
    pass

# Child class
class Child(Parent):
    pass

Grandparent = Grandparent("Grandparent")
print(Grandparent.display()) # This is Grandparent Class

Parent = Parent("Parent")
print(Parent.display()) # This is Parent Class

Child = Child("Child")
print(Child.display()) # This is Child Class



# Multiple Inheritance (Two Parents)

# Father class
class Father:
    
    def Father_class(self):
        return "This is Father class"

# Mother class
class Mother:
    
    def Mother_class(self):
        return "This is Mother class"

# Child class
class Child(Father,Mother):

    def Child_class(self):
        return "This is Child class"

Child = Child()
print(Child.Father_class()) # This is Father class
print(Child.Mother_class()) # This is Mother class
print(Child.Child_class()) # This is Child class



# Abstraction 

from abc import ABC, abstractmethod

# Abstract class (cannot create objects from it)
class Vehicle(ABC):

    def __init__(self,model):
        self.model = model

    @abstractmethod # Abstract method (no implementation)
    def Name(self):
        pass # Child MUST implement this

    def Model(self): # Regular method (has implementation)
        return f"The Model is {self.model}."


# Concrete class (implements all abstract methods)
class Car(Vehicle):
    
    def Name(self,name):        
        self.name = name
        return f"This is a car from {self.name}."


# Concrete class (implements all abstract methods)
class Motorcucle(Vehicle):
    
    def Name(self,name):        
        self.name = name
        return f"This is a motorcucle from {self.name}."


car = Car("SUVs")
print(car.Name("BMW")) # This is a car from BMW.
print(car.Model()) # The Model is SUVs.

motorcucle = Motorcucle("CB300R")
print(motorcucle.Name("Honda")) # This is a motorcucle from Honda.
print(motorcucle.Model()) # The Model is CB300R.



# super()

class Parent:

    def __init__(self,name):
        self.name = name


class Child(Parent):
    
    def __init__(self,name,age):
        self.age = age
        super().__init__(name) # super() is used to call methods from the parent class in a child class
        Parent.__init__(self,name) # wirhout super()


child = Child("Shamim Ahmed Nahid",16)
print(child.name) # Shamim Ahmed Nahid
print(child.age) # 16



# Polymorphism 

class Car:

    def __init__(self, name):
        self.name = name


class BMW(Car):

    def display(self):
        return f"This is a {self.name}"


class Tesla(Car):

    def display(self):
        return f"This is a {self.name}"


bmw = BMW("BMW")
print(bmw.display()) # This is a BMW

tesla = Tesla("Tesla")
print(tesla.display()) # This is a Tesla



# Duck Typing 

# If it has the method, it works!

class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

cat = Cat()
dog = Dog()

def speak_animal(animal):
    print(animal.speak()) # Works if speak() exists

speak_animal(cat) # Meow
speak_animal(dog) # Woof



# Aggregation

# "Has-a" - Both can exist independently

class Author:
    def __init__(self,name):
        self.name = name

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author # Book HAS AN Author

author = Author("Guido van Rossum")
book = Book("Python", author)

print(f"{book.title} by {book.author.name}") # Python by Guido van Rossum



# Composition 

# "Part-of" - Child dies with parent

class Engine:
    def __init__(self,hp):
        self.hp = hp
        
class Car:
    def __init__(self,brand,hp):
        self.brand = brand
        self.engine = Engine(hp) # Engine is PART OF Car
        
car = Car("Toyota", 200)
print(f"{car.brand} has {car.engine.hp}HP engine") # Toyota has 200HP engine



# Nested Classes

# Class inside another class

class School:
    def __init__(self,name):
        self.name = name

    class Student:
        def __init__(self,student_name):
            self.student_name = student_name

# Create school
school = School("NGHS")

# Create student using nested class
student = school.Student("Shamim Ahmed Nahid")

print(f"{student.student_name} studies at {school.name}") # Shamim Ahmed Nahid studies at NGHS



# Static Methods

# Methods that don't need self

class Name:

    @staticmethod
    def name(name):
        return name

# Call without creating object
print(Name.name("Nahid")) # Nahid



# Class Methods

# Methods that use cls (the class)

class Person:

    count = 0 # Uses cls to access class variables.

    def __init__(self,name):
        self.name = name
        Person.count += 1
  
    @classmethod
    def get_count(cls):
        return f"Total: {cls.count}"
    
person = Person("Shamim")
person = Person("Nahid")

print(Person.get_count()) # Total: 2



# Magic Methods / Dunder methods

# Special methods with __

class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages" # __str__() for printing

    def __len__(self):
        return self.pages # __len__() for length
    
    def __contains__(self, title): # checks if an item exists inside an object
        return title in self.title
    
    def __getattr__(self,attr): # Called when accessing an attribute that DOESN'T exist
        return f"Attribute '{attr}' not found!"
    
    def __getitem__(self, keyword): # indexing or key access using
        if keyword in self.title:
            return True
        else:
            return f"{keyword} not found"
        
    def __repr__(self): # Developer representation
        return f"Book({self.title})"
    
    def __eq__(self,other): # Object Comparison
        return self.title == self.pages

book = Book("Python",100)

print(book) # Python has 100 pages
print(len(book)) # 100
print("Python" in book) # True
print(book.name) # Attribute 'name' not found!
print(book["Java"]) # Java not found
print(repr(book)) # Book(Python)
print(book == book) # False



# Encapsulation 

# Access Modifiers

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner  # Public   - accessible anywhere
        self._balance = balance # Protected - convention: "internal use"
        self.__pin = 1234 # Private  - name-mangled by Python

account = BankAccount("Nahid",10000)

print(account.owner) # Nahid
print(account._balance) # 10000
# print(account.__pin) ERROR
print(account._BankAccount__pin) # 1234


# Getters & Setters with @property Decorator

# Make and Access methods look like attributes

class Circle:
    def __init__(self,radius):
        self.radius = radius 

    @property # Getter
    def Radius(self): 
        return f"{self.radius}"

    @Radius.setter # Setter
    def Radius(self,value):
        if value > 0:
            self.radius = value

circle = Circle(5)
print(circle.radius) # 5  (like an attribute, not method!)

circle.radius = 10 # Set like an attribute
print(circle.radius) # 10