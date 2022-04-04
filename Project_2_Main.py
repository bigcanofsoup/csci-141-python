from Project_2 import *
import string
import random

'''
Andrew Guo
Professor Khargonkar
Programming for Data Science
12 March 2021

Project 2 Main File
'''

#First List: Get 4 passwords from password_gen

passList = []
counter = 0

while counter < 4:
    passGen = password_gen(spec_char = '*&@', repeat = False, min_spec = 2, min_upper = 1)
    passList += [passGen]
    counter +=1

print(passList)

#Second List: Determine the validity of each password via password_check should return True for all instances
passCheckList = []
counterCheck = 0

while counterCheck < 4:
    passCheck = check_password(passList[counterCheck], 14, 2, 0, 1)
    passCheckList += [passCheck]

print(passList)

#Second List: Determine the validity of each password via password_check; should return all True.
passCheckList = []
counterCheck = 0

while counterCheck < 4:
    passCheck = check_password(passList[counterCheck], 14, 2, 0, 1) #Included all arguments because they were not optional
    passCheckList += [passCheck]
    counterCheck +=1

print(passCheckList)

#Print lines indicate whether all passwords meet the criteria or not.
if passCheckList[0] == passCheckList[1] == passCheckList[2] == passCheckList[3]:
    print('All passwords meet the criteria.')
else:
    print('One or more passwords does not meet the criteria.')

#Print lines indicate whether all passwords meet the criteria or not.

