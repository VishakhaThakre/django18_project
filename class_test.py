#!/usr/bin/python3

import sys

class Employee:
	empcount = 0
    
	def __init__(self, empname):
		self.empname = empname
        
	def getemp(self):
		print ("employee name = ",self.empname)
        
emp1 = Employee("neeraj")
emp1.getemp()
