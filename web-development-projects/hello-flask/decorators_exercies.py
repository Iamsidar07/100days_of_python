class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(func):
    def wrapper_func(*args):
        if args[0].is_logged_in:
            func(args[0])
    return wrapper_func

@is_authenticated_decorator
def create_blog(user):
    print(f"This is {user.name}'s new blog.")

manoj = User("Manoj")
manoj.is_logged_in = True
create_blog(manoj)

def logging_decorator(func):
    def wrapper_func(*args):
        print(f"You called {func.__name__}{args}")
        result = func(args[0],args[1],args[2])
        print(f"It returned: {result}")
    return wrapper_func

@logging_decorator
def a_function(a, b, c):
    return a * b * c

a_function(1,2,3)