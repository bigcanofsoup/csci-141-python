'''
Andrew Guo
Professor Khargonkar
Project 4 Functions File 
25 April 2021
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Write your def lines and functions below
#The def lines you create must match the specifications exactly
#You cannot change the names of the functions, the variables, or the default arguments
#Expect a large grade penalty if your def lines are not correct
#This file should not contain any function calls or any code that is not part of
#A function definition
#This means any code unindented besides a def line or the import lines at the top

def make_subset(df, region = None, vaccine = None, year = None):
    vaccineFrame = df #brings in the dataFrame into the function
    
    if (region == None and vaccine == None and year == None): #Get copy of VaccineFrame if no arguments are set.
        return vaccineFrame.copy()
    
    region_selection = vaccineFrame['Region'].isin(region or vaccineFrame['Region']) #Checks for user arguments specified in region. If none are found (meaning region is NoneType), then use the whole column, since there is no specification.
    vaccine_selection = vaccineFrame['Vaccine'].isin(vaccine or vaccineFrame['Vaccine']) #Same as above, check for user specifications for vaccines. If NoneType, use all vaccine data.
    year_selection = vaccineFrame['Year'].isin(year or vaccineFrame['Year']) #Same as above, check for user specifications for certain years. If NoneType, use data from all years.
    
    return vaccineFrame.loc[region_selection & vaccine_selection & year_selection] #Finds all rows where each of the above conditions are met.

def make_plot (series_object, title= '', bar = True):
    if bar == True:
        snsgraph = sns.barplot(x = series_object.values, y = series_object.index, orient = 'h')
    else:
        snsgraph = sns.lineplot(x = series_object.index, y = series_object.values)
        plt.xticks(rotation=90)
    plt.title(title)
    return snsgraph