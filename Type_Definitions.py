# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types

name: str = "Shamim Ahmed"
age: int = 17
list_: list = [1,2,3]

print(name) # Shamim Ahmed
print(age) # 17
print(list_) # [1, 2, 3]


# type definitions / Type Hinting in function 

def fun(my_name: str = "Nahid") -> str:
    return my_name

print(fun()) # Nahid


def fun(a: int, b:int) -> int:
    return (a+b)**2

print(fun(2,4)) # 36



# Advanced Type Hints

# List

from typing import List

# “List is an ordered, mutable (changeable) collection of elements.”

list_: List[int] = [1,2,3]
list_.append(5)
print(list_) # [1, 2, 3, 5]


# Tuple

# “Tuple is an ordered but immutable (unchangeable) collection.”

from typing import Tuple

tuple_: Tuple[int, int] = (1,2)
print(tuple_) # (1, 2)

tuple_: Tuple[int, ...] = (1,2,3,4,5)
print(tuple_) # (1, 2, 3, 4, 5)


# Dict

# “Dictionary stores data as key–value pairs.”

from typing import Dict

student: Dict[str, int] = {
    "Age" : 17
}

print(student["Age"]) # 17


# Union

from typing import Union

# “Used when a variable can have multiple possible types.”

def data(data: Union[int, str]) -> str:
    print(data) # 17
    print(type(data)) # <class 'int'>

data(17)

# Modern Python

def data(data: int | str) -> str:
    print(data) # Nahid
    print(type(data)) # <class 'str'>

data("Nahid")


# Optional

# “Means the value can be a type or None.”

from typing import Optional

def output(name: Optional[str]) -> str:
    print(name)

output("Shamim") # Shamim

# Modern Python

def output(name: str | None):
    print(name)

output("Nahid") # Nahid


# Any

# “Allows any type and disables strict type checking.”

from typing import Any

data__: Any = 10
data__ = "Hello World"
print(data__) # Hello World


# Callable

# “Used to type hint a function passed as an argument.”

from typing import Callable 

def output(x: int, fun: Callable[[int],int]) -> int:
    return fun(x)

def square(n: int) -> int:
    return n ** n

print(output(2,square)) # 4


# Literal

# “Restricts a variable to specific fixed values.”

from typing import Literal

def activity(active: Literal["Online","Offline"]):
    print(active)

activity("Online") # Online


# TypedDict

# “Creates a dictionary with fixed key types.”

from typing import TypedDict 

class User(TypedDict):
    name : str
    age : int

user: User = {
    "name" : "Shamim",
    "age" : 17
}

print(user) # {'name': 'Shamim', 'age': 17}


# TypeVar

# “Used to create generic types.”

from typing import TypeVar, List

T = TypeVar("T")

def iteam(iteams: List[T]) -> T:
    return iteams[0]

print(iteam([1,2,3,4,5])) # 1


# Generic

# “Allows classes to work with multiple types safely.”

from typing import Generic, TypeVar

T = TypeVar("T")

class Name(Generic[T]):
    def __init__(self,name: T):
        self.name = name

    def get(self) -> T:
        return self.name
    
name = Name("Shamim Ahmed")
print(name.get()) # Shamim Ahmed


# Protocol

# “Defines required methods for objects (structural typing).”

from typing import Protocol

class Student(Protocol):
    def say(self) -> str:
        ...

class Me:
    def say(self) -> str:
        return "I'm a student"

def display(me: Student) -> str:
    return me.say()

object = Me()
print(display(object)) # I'm a student