"""
Elon Musk plans to retire on Mars. One year on Mars is 687 Earth days. One year on Earth is 365.25 Earth days.
So, for example, if he stays on Mars for 16 Mars years, that’s about 30 Earth years.
Write a program that solicits a single input from the user: a number of Mars years. Your program should convert
the Mars years to Earth years using the information given above. Cast this value to an int.
You must format the program's interaction as illustrated in the following examples. Do not vary the phrasing,
capitalization, spacing, etc. You must also write a properly styled, easily readable and understandable program.
Enter number of Mars years: 10
This is about 18 years on Earth.
Your program should work for any non-negative numeric input provided by the user. Other inputs will not be
tested. Save this program in a file called Mars_to_Earth.py
"""
#Andrew Guo, Programming for Data Science, Professor Khargonkar, 16 February 2021. Project 1 Mars_to_Earth.py File.

EARTH_DAY_IN_YEARS = 365.25 
MARS_DAY_IN_YEARS = 687 

oneMarsYearonEarth = MARS_DAY_IN_YEARS/EARTH_DAY_IN_YEARS #Calculates how long one year's worth of days on Mars is on Earth. 

marsInput = float(input('Enter number of Mars years: ')) #user input changed to type float for calculation below.

earthYears = print(('This is about'),int(oneMarsYearonEarth * marsInput), ('years on Earth.')) #multiply the user's input for number of Mars years by the duration of one Mars year on Earth. 