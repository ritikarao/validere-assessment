#!/usr/bin/env python3

import requests
import pandas as pd
import os

URL = "https://www.crudemonitor.ca/savePHPExcel.php"

print("Enter the name of your crude oil and its acronym:")
name = input()
acronym = input()

name.title()
acronym.upper()

print("Enter the start and end dates for your search, in the format DDMMYYYY:")
date1 = input()
date2 = input()

database = "crudes"

form_data = {
    "date1noscript": "",
    "date2noscript": "",
    "trendProperty": "AbsoluteDensity",
    "acr": acronym,
    "name": name,
    "db": database,
    "basicanalysis[]": "AbsoluteDensity",
    "options": "on",
    "date1": date1,
    "date2": date2,
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

os.remove('Density.csv')
