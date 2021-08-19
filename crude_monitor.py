#!/usr/bin/env python3

import requests
import pandas as pd
import os
import argparse

URL = "https://www.crudemonitor.ca/savePHPExcel.php"

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--crude_acronym", required = True, help = "crude oil acronym")
ap.add_argument("-n", "--name", required = True, help = "crude oil name")
ap.add_argument("-i", "--start_date", required = True, help = "start date in the format YYYY-MM-DD")
ap.add_argument("-f", "--end_date", required = True, help = "end date in the format YYYY-MM-DD")
ap.add_argument("-o", "--operation", required = True, help = "operation in the format greater_than_equal_to or >=")
ap.add_argument("-l", "--limit", required = True, help = "threshold value for density search")
args = ap.parse_args()

acronym = args.crude_acronym
name = args.name
date1 = args.start_date.split("-")
start_date = date1[2] + date1[1] + date1[0]
date2 = args.end_date.split("-")
end_date = date2[2] + date2[1] + date2[0]
operation = args.operation
limit = float(args.limit)

name.title()
acronym.upper()

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


if operation == 'greater_than' or operation == '>':
    df.drop(df[df.Density <= limit].index, inplace = True)
elif operation == 'lesser_than' or operation == '<':
    df.drop(df[df.Density >= limit].index, inplace = True)
elif operation == 'greater_than_equal_to' or operation == '>=':
    df.drop(df[df.Density < limit].index, inplace = True)
elif operation == 'lesser_than_equal_to' or operation == '<=':
    df.drop(df[df.Density > limit].index, inplace = True)
elif operation == 'equal_to' or operation == '=' or operation == '==':
    df.drop(df[df.Density != limit].index, inplace = True)

df = df.reset_index(drop = True)

if df.empty:
    print("No results for the dates and condition specified!")
else:
    print(df)

os.remove('Density.csv')
