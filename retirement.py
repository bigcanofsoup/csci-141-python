"""
Speaking of retirement, you need to start saving early if you’re going to make it to Mars. Many employers offer
workplace retirement accounts. 
Money is deducted (taken out) of an individual’s salary and is put into a separate
account that is not accessible (usually) until retirement. Individuals get to select the amount they want to save per
paycheck.
Write a program that calculates the amount of each equal deduction per paycheck, and how many extra dollars
should be added to the last payment to hit the target. Your program will solicit two inputs from the user: a target
amount in whole dollars (no cents) and the number of times an individual is paid per year. Save this program in3#a file called retirement.py.
Program execution should look like what is shown below. Pay special attention to formatting, spacing, and
capitalization of the input and output lines.
Enter total amount to save: 10000
Enter number of paychecks per year: 12
You must make 11 deductions of $833 and one final deduction of $837 to save $10000
Enter total amount to save: 3600
Enter number of paychecks per year: 24
You must make 23 deductions of $150 and one final deduction of $150 to save $3600
Note that the output is the same whether or not the final payment is a different value. You can assume that the
inputs for the target and number of paychecks will be positive integers, and your program should work for any
such inputs.
"""
#Andrew Guo, Programming for Data Science, Professor Khargonkar, 16 February 2021. Project 1 retirement.py File. 

savingsInput = int(input('Enter total amount to save: ')) 
paychecksInput = int(input('Enter number of paychecks per year: ')) 

deductionsNeeded = paychecksInput-1 #All paychecks excluding final deduction
deductionWorth = savingsInput//paychecksInput #Int. division for whole number for deduction worth, excluding final deducion
finalDeduction = savingsInput-(deductionWorth*deductionsNeeded) # final deduction worth: savings wanted - (deduction amt. excluding final deduction * amt. of deductions needed, excluding final deduction)

print('You must make',deductionsNeeded,'deductions of $' + str(deductionWorth)+ ' and one final deduction of $' + str(finalDeduction) +' to save $' + str(savingsInput))