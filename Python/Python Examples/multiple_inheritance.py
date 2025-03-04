#!/usr/bin/env python3

print(
"""
From:
https://www.geeksforgeeks.org/multiple-inheritance-in-python/
"""
)



print(
'''
# Python Program to depict multiple inheritance
# when method is overridden in both classes
'''
)
class Class1:
	def m(self):
		print("In Class1") 
		
class Class2(Class1):
	def m(self):
		print("In Class2")
		
class Class3(Class1):
	def m(self):
		print("In Class3")  
		
class Class4(Class2, Class3):
	pass  
	
obj = Class4()
obj.m()

print("The chosen method is from the class first in the list")
print("-"*100)



# Python Program to depict multiple inheritance
print("# when every class defines the same method")


class Class1:
	def m(self):
		print("In Class1") 
		
class Class2(Class1):
	def m(self):
		print("In Class2")
		
class Class3(Class1):
	def m(self):
		print("In Class3")     
		
class Class4(Class2, Class3):
	def m(self):
		print("In Class4")   
		
obj = Class4()
obj.m()

Class2.m(obj)
Class3.m(obj)
Class1.m(obj)

print("when the super class's method is called with a subclass object, the super class's methods are chosen")
print("-"*100)


# Python Program to depict multiple inheritance 
print(
"""
# when we try to call the method m for Class1, 
# Class2, Class3 from the method m of Class4
"""
)


class Class1:
	def m(self):
		print("In Class1") 
		
class Class2(Class1):
	def m(self):
		print("In Class2")
		
class Class3(Class1):
	def m(self):
		print("In Class3")	 
		
class Class4(Class2, Class3):
	def m(self):
		print("In Class4") 
		Class2.m(self)
		Class3.m(self)
		Class1.m(self)
		
obj = Class4()
obj.m()
print("-"*100)
print(
"""
# Python Program to depict multiple inheritance
# when we try to call m of Class1 from both m of
# Class2 and m of Class3
"""
)
class Class1:
	def m(self):
		print("In Class1") 
		
class Class2(Class1):
	def m(self):
		print("In Class2")
		Class1.m(self)
		
class Class3(Class1):
	def m(self):
		print("In Class3")
		Class1.m(self) 
		
class Class4(Class2, Class3):
	def m(self):
		print("In Class4") 
		Class2.m(self)
		Class3.m(self)
		
obj = Class4()
obj.m()


print(
	"""
The output of the above code has one problem associated with it, the method m of Class1 is called twice. Python provides a solution to the above problem with the help of the super() function. Let’s see how it works.
	"""
)

print("-"*100)

# Python program to demonstrate
# super()

class Class1:
	def m(self):
		print("In Class1")
		
class Class2(Class1):
	def m(self):
		print("In Class2")
		super().m()
		
class Class3(Class1):
	def m(self):
		print("In Class3")
		super().m()
		
class Class4(Class2, Class3):
	def m(self):
		print("In Class4") 
		super().m()
		
obj = Class4()
obj.m()

print(
"""
Super() is generally used with the __init__ function when the instances are initialized. The super function comes to a conclusion, on which method to call with the help of the method resolution order (MRO).
"""
)

print("-"*100)
print(
"""
Method resolution order:

In Python, every class whether built-in or user-defined is derived from the object class and all the objects are instances of the class object. Hence, the object class is the base class for all the other classes.
In the case of multiple inheritance, a given attribute is first searched in the current class if it’s not found then it’s searched in the parent classes. The parent classes are searched in a left-right fashion and each class is searched once.
If we see the above example then the order of search for the attributes will be Derived, Base1, Base2, object. The order that is followed is known as a linearization of the class Derived and this order is found out using a set of rules called Method Resolution Order (MRO).
To view the MRO of a class: 


Use the mro() method, it returns a list 
Eg. Class4.mro()
Use the _mro_ attribute, it returns a tuple 
Eg. Class4.__mro__ 
"""
)

print(Class4.mro())
print(Class4.__mro__)

print("-"*100)


# Python program to demonstrate
# super()

class Class1:
	def m(self):
		print("In Class1")
		
class Class2(Class1):
	def m(self):
		print("In Class2")
		super().m()
		
class Class3(Class1):
	def m(self):
		print("In Class3")
		super().m()
		
class Class4(Class2, Class3):
	def m(self):
		print("In Class4") 
		super().m()
		
print(Class4.mro())		 #This will print list
print(Class4.__mro__)	 #This will print tuple
