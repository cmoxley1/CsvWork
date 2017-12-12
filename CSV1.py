#!/usr/bin/python3
import csv
import pandas as pd
import numpy as np
import arrow

now = arrow.now()
date = now.format('DD-YYYYMM')


now1 = arrow.now()
date2 = now1.shift(days= -1).format('DD')
print("{}{}".format(date,date2))
now2 = arrow.now()
date3 = now2.shift(days= -1).format('DD-YYYYMM')

fincvs = csv.reader(open('{}{}DailyDroppedThreats.csv'.format(date3,date2)))
dist = 0
for row in fincvs:
	_dist = row[2]
	try:
		_dist = int(_dist)
	except ValueError:
		_dist = 0
		
	dist+= _dist	
print(dist)
					
df =  pd.read_csv('{}{}CountryandIOCDroppedThreats.csv'.format(date,date2),sep=',')
df1 = df.set_index("Rule")
ll1 = df1.at["External-Dynamic-Block-Outbound","Count"]
ll2 = df1.at["External-Dynamic-Block-Inbound","Count"]
ll4 = df1.at["Country Code Blocks Destination","Count"]
ll5 = df1.at["Country Code Blocks Source","Count"]
ll3 = ll1+ll2
ll6 = ll4+ll5

print(ll3)
print("Palo Alto Total")
total = ll3+dist
print(total)
print("Palo Alto Geo Total")
print(ll6)