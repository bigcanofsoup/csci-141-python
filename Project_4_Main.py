'''
Andrew Guo
Professor Khargonkar
Project 4 Main Program File 
25 April 2021
'''
#Do not change any of the import lines
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Project_4 import *

#Part 1: Data QC
#Do not change the order of lines
#Maintain the original structures (if there is a lambda, use a lambda etc)
#You can copy and paste in the line
#vaccine.head()
#or from the command line
#print(vaccine.head())
#to view the data frame
#comment these lines out before you turn in your project

#Read in the data
#Old Line: vaccine = pd.read_csv(vaccine_data.csv)
vaccine = pd.read_csv('vaccine_data.csv')

#Assign column names
#Old Line: vaccine.columns = Region,Vaccine,Year,Percentage 
vaccine = vaccine.set_axis(['Region','Vaccine','Year','Percentage'], axis = 1)

#Update region names to replace & with and and remove spaces
#Old Line: vaccine = vaccine.replace(to_replace = '&', value = 'and')
vaccine['Region'] = vaccine['Region'].replace(['&',' '], ['and', '_'], regex = True)

#Change type of Year column to a string
#Old Line: str(vaccine['Year'])
vaccine['Year'] = vaccine['Year'].astype(str)

#Create description column
#The dictionary line is correct, you must use the dictionary
mappings = {'BCG':'tuberculosis', 'DTP1':'diphteria_pertussis_tetanus','DTP3': 'diptheria_pertussis_tetanus',\
'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease','HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
'HIB1':'Haeomphilus influenza', 'HIB3':'Haemophilus influenza','IPV1': 'polio','IPV3': 'polio', 'POL3': 'polio','PCV3':'pneumococcal disease', 'RCV1':'rubella',\
'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}

#Old Line: vaccine['Description'] = vaccine.apply(lambda x: mappings(x))
vaccine['Description'] = vaccine['Vaccine'].apply(lambda x: mappings.get(x))

#Check the data frame before continuing
#Create a data frame called BCG_2019 that contains the rows for BCG vaccine for 2019
BCG_2019 = make_subset(vaccine, vaccine = ['BCG'], year = ['2019'])

#From the data frame you made, create a Series called BCG2019_Series with Region  as the index and Percentage as the values
BCG2019_DataFrame = pd.DataFrame(BCG_2019).set_index('Region')
BCG2019_Series = pd.Series(data = BCG2019_DataFrame['Percentage'])

#Create a barplot for the percentage outreach (Percentage) of BCG vaccine by region in 2019.
make_plot(BCG2019_Series, title = 'Percentage Outreach of BCG Vaccine by Region in 2019')

#Create a data frame called DPT1_Years that contains the rows for DPT1 vaccinations in the East Asia and Pacific region
DPT1_Years = make_subset(vaccine, region = ['East_Asia_and_Pacific'],  vaccine = ['DTP1'])

#From the data frame you made, create a Series called DPT1_series that has Year as the index and Percentage as the values
DPT1_DataFrame = pd.DataFrame(DPT1_Years).set_index('Year')
DPT1_series = pd.Series(data = DPT1_DataFrame['Percentage'])

#Create a line plot of the data stored in DPT1_series with the title: DPT1 Vaccinations by Year in East Asia and Pacific Region
make_plot(DPT1_series, title = 'DPT1 Vaccinations by Year in East Asia and Pacific Region', bar = False)

#Bibliography:
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
#https://www.geeksforgeeks.org/replace-values-in-pandas-dataframe-using-regex/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html?highlight=replace
#https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/05_add_columns.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html
#https://realpython.com/python-or-operator/
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html 





