import random

# from random import randint -> import from module

# Basics
print("Hello world")  # Print a string into the console.
name = input("What is your name? ")  # Input from user always as string
print(f"Hello, {name}")

# This is comment which is ignored by machine
print("This is code.")

# variables
# give a name to a piece of data just like label a box
my_name = "Monika Sidar"  # My baby's name
my_age = 20

# += operator
# say "Take it's previous value and add to it"
my_age += 1
print(my_age)  # my_age is now 21


# Data types
# Integers (Whole numbers)
my_number = 354

# Floats (Floating point numbers, decimal numbers)
my_float = 3.141
# comment is looking very sexy
# String (Just a string of characters)
my_string = "Hello"

# boolean -> True|False

is_adult = True
print(type(is_adult))  # type, check the data type
print(is_adult)

# String concatenation
# You can add a string to another string to create a new string
wish = "Hello" + "Monu"  # becomes HelloMonu
print(wish)

# Escaping string
# As double quote is special it denotes the string if you want to use double quote, you need to escape it with "\"

speech = 'She said: "Hi"'
print(speech)

# f-string
# I can insert a variable into a string using f string, insert a variable between {}
days = 365
print(f"There are {days} days in a year.")

# Converting data types
# int() -> converting into integer
# float() -> converting into float
# str() -> converting into string
n = "34"
n_as_int = int(n)
n_as_float = float(n)
n_as_string = str(n_as_int)

print(n_as_string)

# Checking data types
# use type function to check data types
print(type(n_as_string))

# Maths
print(1 + 2)  # + add
print(1 - 2)  # - substraction
print(2 * 2)  # * multiplication
print(
    2 / 2
)  # / division -> always return a float data type, use // to do floor division (return a integer)
print(2**3)  # ** exponential
print(3 % 2)  # % returns remainder


# functions
def my_function():
    print("Hello")
    name = input("What is your name? ")
    print(f"Hello, {name}")


# Calling a function
my_function()


# function with inputs
def add(n1, n2):
    print(n1 + n2)


add(2, 3)

# function with output


def multiplication(n1, n2):
    return n1 * n2


result = multiplication(2, 3)
print(f"multiply of 2 and 3 is: {result}")

# variable scope
# variable created inside the function are destroyed once the function has executed.

pi = 3.14


def pi_function():
    pi = 10
    print(pi)  # 10


print(pi)  # 3.14
pi_function()

# keyword argument

# When calling function we can provide keyword argument or simply just the value
# if we provide keyword argument then order does not matter but, if we simple put just value it matters


def divide(n1, n2):
    result = n1 / n2
    print(result)


divide(10, 5)
divide(n2=5, n1=10)

# Conditionals

num = 5
if num > 2:
    print("Greater than 2.")

age = 14

if age > 16:
    print("Can drive.")
else:
    print("Can't drive.")

weather = "snow"
if weather == "sunny":
    print("bring sunglass.")
elif weather == "rain":
    print("bring umbrella.")
elif weather == "snow":
    print("bring some gloves with you.")

# and
score = 58
if score > 50 and score < 60:  # if score is greater than 50 and smaller than 60
    print("Your grade is C.")

# or
person_age = 200
if person_age > 100 or person_age < 16:
    print("Can't drive")

# not

if not 3 < 1:
    print("Something")

# Comparasion operators
# == is equal to
# != is not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# Loops
# while loop

count = 1
while count <= 10:
    print(count)
    count += 1

# for loop
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# If the item is not needed I can use _
for _ in range(90):
    print("I love you monu.")

# break -> exit out of loop
scores = [23, 45, 67, 88]
for s in scores:
    if s > 50:
        break
    print(s)
# continue -> skip the iteration of the loop

x = 1
while x < 100:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

# Infinite loop
# while True:
#     print("I am survivor.")

# List like array in javaScript
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]
list3 = list1 + list2
print(list3, type(list3))

# adding an item to the list
all_fruits = ["apple", "banana"]
all_fruits.append("Orange")
print(all_fruits)

# List indexing starts from 0 it can also start from -1 if you want to start from the end
print(all_fruits[0])  # apple
print(all_fruits[-1])  # orange

print(all_fruits[-2])  # second item from the last-> banana

# List slicing

# by index syntax and with colon symbol we can slice
# start index is included but end is not
# Do not change the original list
print(all_fruits[2:3], all_fruits)

# Built in functions
# range function
# range(start,end,step)
# start included, end is excluded
for i in range(10, 0, -2):
    print(i)

# randomisation
# random function comes from random module
# randint(start,end)
# start and end both included
random_number = random.randint(2, 10)
print(random_number)

# round function to round off
print(round(4.65))

# abs (absolute function to get absolute value)
# basically removes any -ve signs
print(abs(-5))

# Modules
# importing

list4 = [1, 2, 3]
print(f"x: {random.choice(list4)}")


# Classes and Objects
# Created using class keyword, class name in python are in PascalCase

# class Car:
#     pass
# my_toyota = Car() # Creating an Object from class

# class methods
# You can create a function inside the class that is known as method

# class Car:
#     size = "Large"
#     colour = "Orange"
#     def drive(self):
#         # self -> Car object like "this" keyword in javascript
#         print("move:", self)
# my_toyota = Car()
# my_toyota.drive()
# print(my_toyota.colour)

# __init__ method
# __init__ method is called every time a new object is created from the class
# class Car:
#     size = "Large"
#     colour = "Orange"
#     def __init__(self):
#         print("Building Car...")
#     def drive(self):
#         # self -> Car object like "this" keyword in javascript
#         print("move:", self)
# my_toyota = Car()
# my_toyota.drive()
# print(my_toyota.colour)

# Class properties
# We can create a variable in the init() of a class so that all the objects created from the class has access to that variable


class Car:
    size = "Large"
    colour = "Orange"

    def __init__(self, name):
        self.name = name
        print("Building Car...")

    def drive(self):
        # self -> Car object like "this" keyword in javascript
        print("move:", self)

    def info(self):
        print(f"Owner of Car: {self.name}")


my_toyota = Car("Monu")
my_toyota.drive()
my_toyota.info()
# print(my_toyota.colour)


# class inheritance
# When you create a class you can inherit the properties and methods of the another class
class Animal:
    def breath(self):
        print("Breathing...")


class Fish(Animal):
    print(Animal)

    def breath(self):
        super().breath()
        print(super())
        print("underwater")


nemo = Fish()
nemo.breath()
