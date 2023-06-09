# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:24:20 2021

@author: nzrh
"""
import pandas as pd
import numpy as np

#  DATA COLLECTION from CSV
df = pd.read_csv('CTG.csv')
#print(data)
print(df.head(5))
print('Shape: ', df.shape)


to_drop = ['FileName','SegFile' ,'b' ,'e' ,
           'DL', 'DS', 'DP' ,'DR' ,'Width','Nmax','Nzeros', 
           'A', 'B', 'C', 'D', 'E', 'AD', 'DE', 'LD', 'FS' ,'SUSP', 'CLASS']
print(df.iloc[0:3,0:])
df.drop(to_drop, inplace=True, axis=1) #OR    df.drop(columns=to_drop, inplace=True)
print(df.iloc[0:3,0:])

df["Date"] = pd.to_datetime(df["Date"]) 
print(df["Date"])
print(df['Date'].dt.year)
print(df['Date'].dt.month)

#new column (month, year)
df['Month']= df['Date'].dt.month
df['Year'] = df['Date'].dt.year
print(df)

print('Remove rows with Na, NaN, NaT:')
print(df.dropna()) # remove  rows with Na, NaN, NaT

