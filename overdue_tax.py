"""
If you fail to pay income tax in a timely manner and you owe the government (or the state you live in) money,
you are subject both to a penalty and interest on the amount owed. Even if you are living on Mars, if you are a
US citizen, you have to file Federal taxes.
Suppose that during your stay-cation on Mars, the interstellar mail took too long and you haven’t paid your taxes
on time . . . your tax return was literally lost in space. 
You owe the original tax plus a penalty that is 6% of the tax amount – for our purposes the penalty will always be 6%. 
You also owe interest on the tax (not the penalty,just the tax). The amount of interest depends on the current yearly rate and the amount of interest you owe depends
on how many days overdue the tax is. 
In the file overdue_tax.py, you have been code for a program that provides constants for the length of a year and
the penalty rate, and solicits the tax owed, the number of days overdue, and the interest rate from the user. The
program is supposed to calculate the total amount owed, but the program is incorrect.
Your job is to debug the program. Debugging the code means that you edit the lines in place. You should
not add lines, delete lines, or move the order of lines. Correct the lines as they are and preserve as much of
the original code as possible.
"""
#Andrew Guo, Programming for Data Science, Professor Khargonkar, 16 February 2021. Project 1 overdue_tax.py File.

PENALTY_RATE = 0.06 #Do not change
EARTH_YEAR = 365 #Do not change

tax = input('Enter amount of tax owed: ') #Do not change, will be in format $100
rate = input('Enter interest rate: ') #Do not change, will be in format 4%
late = int(input('Enter number of days overdue tax is: ')) #Do not change, will be an integer

penalty = PENALTY_RATE * float(tax[1:]) #changed tax to type float for penalty calculation; sliced to remove dollar sign

interest = (float(tax[1:]) * float(rate[0:-1])/100)* (late/EARTH_YEAR) #changed rate to type float for interest calculation; sliced to remove percent sign

total = float(tax[1:]) + float(interest) + float(penalty) #Change everything to a float to add up numbers properly, added slicing for tax so dollar sign is removed

print('Your total payment is', round(total)) 
