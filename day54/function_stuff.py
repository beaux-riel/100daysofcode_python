# Had to try this out because it was a bit of a lightbulb moment

# def outer_function():
#     print("I'm outer")
    
#     def nested_function():
#         print("I'm inner")
        
#     return nested_function

# inner_function = outer_function()
# inner_function()

# Python Decorator Function

import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(3)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")
    
@delay_decorator
def say_bye():
    print("Bye")
    
def say_greeting():
    print("How are you?")
    
say_hello()
say_bye()
say_greeting()