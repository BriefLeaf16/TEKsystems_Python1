#import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. 
When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print('Invoking function with mix of default arguements')
introduction_with_mix_of_default_args('John')

print('Invoking function that returns values')
print(product_of_two_num(9,8))


print('Function with arbitrary functions')
print(add_all_nums(1,2,3))


print('This is the equivalent of the lambda function')
print(double(12))


print('This is the recursive fibonacci function')
print(fib(9))


print('This is the function level scoping')
print(subtract(5,2))


print('This is the palindrome function')
print(palindrome_str())


print('Not sure if I was even suppose to make a function, but here is the boolean Bob function')
print(are_you_bob())
