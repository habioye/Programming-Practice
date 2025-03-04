#!/usr/bin/env python3
import sys
import os

print("Print Test1")
oldoutput = sys.stdout
sys.stdout = open(os.devnull, 'w')
print("Print Test2")
sys.stdout = oldoutput
print("Print Test3")

print(
	"""
	Only the print output of the for Test3 is shown
	"""
)


def dummy (*args):
	pass
oldprint = print	
print = dummy


print("Print Test4")
print = oldprint


print("Print Test5")


print(
	"""
	Only the print output of the for Test5 is shown
	"""
)
s = "temperory string"
s = "temprorary string"
print(s)
