#!/usr/bin/python3
import csv
import pandas as pd
import arrow
import fnmatch
import os 

# get current date and subtract 1 day and change date formate
nv = arrow.now()
date = nv.shift(days= -1).format('YYYYMMDD')

# find the filename and assign it to a variable 
for file in os.listdir('.'):
	if fnmatch.fnmatch(file, '??-{}DailyDroppedThreats.csv'.format(date)):
		file_1 = file
		print(file_1)
		
for file3 in os.listdir('.'):
	if fnmatch.fnmatch(file3, '??-{}CountryandIOCDroppedThreats.csv'.format(date)):
		file_2 = file3
		print(file_2)

# Read the file, index the file, and get sum of the "count" column 
df1= pd.read_csv('%s'% file_1,sep=',') 
df2 = df1.set_index("Threat/Content Name")
total_1 = df2['Count'].sum()
# Read the file, index the file 
df3 =  pd.read_csv('%s' % file_2,sep=',')
df4 = df3.set_index("Rule")

# define each cell in the index that I want to target 
cell01 = df4.at["External-Dynamic-Block-Outbound","Count"]
cell2 = df4.at["External-Dynamic-Block-Inbound","Count"]
cell3= df4.at["Country Code Blocks Destination","Count"]
cell4 = df4.at["Country Code Blocks Source","Count"]

# ADD cell values that I need
total_2 = cell01+cell2

total_3 = cell3+cell4

total = total_2 +total_1

print(total_1)
print (total_2)
print("--------<-Total 1")
print(total)
print("--------<-Total 2")
print(total_3)