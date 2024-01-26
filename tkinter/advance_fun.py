# Functions with default value
def add(a=1, b=2, c=3):
    return a + b + c

# print(add(c=10))

# Functions with unlimited arguments
def multiply(*unlimted_args):
    print(unlimted_args, type(unlimted_args))
    result = 1
    for n in unlimted_args:
        result *= n
    print(result)

multiply(1,23,23,11,23,32,12,34)

def unlimited_add(*args):
    # args -> tupple
    return sum(args)

print(unlimited_add(1,2,3,4,5))


# **kwargs: Many keyworded Arguments
# Unlimited keyword argument

def calculate(**kargs):
    # kargs-> dictionary
    print(kargs, type(kargs))
    for (key,value) in kargs.items():
        print(key,value)
    print(kargs["add"])

# def calculate(**unlimited_keyword_args):
#     # kargs-> dictionary
#     print(unlimited_keyword_args, type(unlimited_keyword_args))

calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kargs):
        self.make = kargs.get("make") # return None if it is undefined
        self.model = kargs.get("model")    
        self.color = kargs.get("color")    
        self.seats = kargs.get("seats")    

my_car = Car(make="BMW", model="GTM 32", color="red")
print(my_car.color, my_car.seats)