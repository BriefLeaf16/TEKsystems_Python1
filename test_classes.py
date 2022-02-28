from arthmetic import *
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the user’s username, password, registration date, and more. 
Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. 
You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
print(type(ar.print_self()))

#TODO: create several more instance of the Arithmetic class and add different values
print("Next is ar1")
ar1 = Arithmetic(8,9)
print(ar1.multiply())
print(ar1.remainder())


print("Next is ar2")
ar2 = Arithmetic(20,50)
print(ar2.remainder())
print(ar2.subtract())


print('Next is ar3')
ar3 = Arithmetic(3.14,9.80)
print(ar3.add())
print(ar3.divide())


print('Next is ar4')
ar4 = Arithmetic(-7, -4)
print(ar4.multiply())
print(ar4.divide())
print(ar4.remainder()) 

