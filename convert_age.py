"""
Write a program that allows the user to input their age on a home planet and then converts their age to the selected
destination planet. The program will provide the output in the requested format. You have been given two lines
of code that you cannot change in any way which must be used for your program in the file convert_age.py.
The program will take three inputs: a number for selecting home planet, age on home planet and a number to
select the destination planet.
Program execution should look like what is shown below. Pay special attention to formatting, spacing, and
capitalization of the input and output lines.
Select your home planet: 1 for Mercury, 2 for Mars, 3 for Jupiter, 4 for Saturn, 5 for Neptune: 1
Enter your age on your home planet: 10
Select a destination planet: 1 for Mercury, 2 for Mars, 3 for Jupiter, 4 for Saturn, 5 for Neptune: 2
Your age on Mars is about 1 years
You can assume that the inputs for age will always be positive numbers, but they may have fractional components.
You can also assume that the inputs for selecting a planet will always be one of the integers 1,2,3,4, or 5. The
final value computed should be an integer. No other inputs will be tested.
"""
#Andrew Guo, Programming for Data Science, Professor Khargonkar, 16 February 2021. Project 1 convert_age.py File.

D_PER_Y_PLANETS = [87.97, 687, 4331.87, 10760.27, 60189.55] #Do not change
PLANETS = ['Mercury', 'Mars', 'Jupiter', 'Saturn', 'Neptune'] #Do not change

homePlanet = int(input('Select your home planet: 1 for Mercury, 2 for Mars, 3 for Jupiter, 4 for Saturn, 5 for Neptune: ')) 
homeAge = float(input('Enter your age on your home planet: ')) #assume person has lived on home planet for homeAge years

destPlanet = int(input('Select a destination planet: 1 for Mercury, 2 for Mars, 3 for Jupiter, 4 for Saturn, 5 for Neptune: ')) 
destAge = (homeAge * D_PER_Y_PLANETS[homePlanet-1]) / D_PER_Y_PLANETS[destPlanet-1] #Destination age: (number of years spent on home planet * length of 1 year on home) / (the length of one year in destination planet) 
planetSelection = PLANETS[destPlanet-1] #Creates string to indicate what planet is being travelled to, subtract by 1 to account for pos. 0. 

print('Your age on',planetSelection,'is about',int(destAge),'years') 



