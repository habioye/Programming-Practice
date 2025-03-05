#!/usr/bin/env python3

#~ ❯ Python3                                                         06:10:47 PM
#Python 3.13.1 (main, Dec  3 2024, 17:59:52) [Clang 16.0.0 (clang-1600.0.26.4)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
>>> val = 1
>>> print(val)
1
>>> other = 3
>>> print(other)
3
>>> print(val + other)
4
>>> val = other-val
>>> print(val)
2
>>> def addthree(n):
...     n+=3
...     return n
...
>>> print(addthree(val))
5
>>> print(val)
2
>>> def subtractten(number):
...     number-=10
...     return number
...
>>> def subtracttwo(number):
...     number-=2
...
>>> print(subtracttwo(val))
None
>>> def subtracttwo(number):
...     number-=2
...
>>>
>>> def subtracttwo(number):
...     number-=2
...     pass
...
>>> def subtracttwo(number):
...     number-=2
...     return 1
...     return 2
...     return number
...
>>> print(subtracttwo(number))
Traceback (most recent call last):
	File "<python-input-17>", line 1, in <module>
		print(subtracttwo(number))
											^^^^^^
NameError: name 'number' is not defined
>>> print(subtracttwo(val))
1
>>> print(val)
2
>>> def subtracttwo(number):
...     number-=2
...
...     return 2
...     return number
...
>>> print(subtracttwo(val))
2
>>> print(val)
2
>>> def subtracttwo(number):
...     number-=2
...
...
...     return number
...
>>> print(subtracttwo(val))
0
>>> print(val)
2
>>>
