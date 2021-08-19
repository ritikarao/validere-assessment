#!/usr/bin/env python3

import requests
import pandas as pd
import os

URL = "https://www.crudemonitor.ca/savePHPExcel.php"

print("Enter the name of your crude oil and its acronym:")
crude_name = input()
crude_acronym = input()

crude_name.title()
crude_acronym.upper()

print("Enter the start and end dates for your search, in the format DDMMYYYY:")
start_date = input()
end_date = input()

database = "crudes"

form_data = {
    "date1noscript": "",
    "date2noscript": "",
    "trendProperty": "AbsoluteDensity",
    "acr": crude_acronym,
    "name": crude_name,
    "db": database,
    "basicanalysis[]": "AbsoluteDensity",
    "options": "on",
    "date1": start_date,
    "date2": end_date,
    "format": "Export.CSV",
    "daterangepicker_start": "",
    "daterangepicker_end": "",
}

data = requests.post(url=URL, data=form_data)

file = open("Density.csv", "wb")
file.write(data.content)
file.close()

df = pd.read_csv('Density.csv', usecols = ['Date', 'Density (kg/m^3)'])
df.rename(columns = {'Density (kg/m^3)':'Density'}, inplace = True)

print("Enter your search operation (greater than, lesser than, equal to, greater than equal to, etc:")
operation = input()

operation.title()

print("Enter your limit value:")
limit = input()

if operation == 'Greater Than' or operation == '>':
    df.drop(df[df.Density <= float(limit)].index, inplace = True)
elif operation == 'Lesser Than' or operation == '<':
    df.drop(df[df.Density >= float(limit)].index, inplace = True)
elif operation == 'Greater Than Equal To' or operation == '>=':
    df.drop(df[df.Density < float(limit)].index, inplace = True)
elif operation == 'Lesser Than Equal To' or operation == '<=':
    df.drop(df[df.Density > float(limit)].index, inplace = True)
elif operation == 'Equal To' or operation == '=' or operation == '==':
    df.drop(df[df.Density != float(limit)].index, inplace = True)

df = df.reset_index(drop = True)

if df.empty:
    print("No results for the dates and condition specified!")
else:
    print(df)

os.remove('Density.csv')
