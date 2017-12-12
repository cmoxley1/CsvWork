#!/usr/bin/python3
import csv
import pandas as pd
import numpy as np
import arrow

<<<<<<< HEAD
nv = arrow.now()
 
date = nv.format('DD-YYYYMM')
date2 = nv.shift(days= -1).format('DD')
date3 = nv.shift(days= -1).format('DD-YYYYMM')

df1= pd.read_csv('{}{}filename.csv'.format(date3,date2),sep=',')
df2 = df1.set_index("selectColumn")
total_1 = df2['Count'].sum()

		
df3 =  pd.read_csv('{}{}filename.csv'.format(date,date2),sep=',')
df4 = df3.set_index("selectColumn")

cell01 = df4.at["row","column"]
cell2 = df4.at["row,"column"]
cell3= df4.at["row","column"]
cell4 = df4.at["row","column"]
total_2 = cell01+cell2
total_3 = cell3+cell4
total = total_2 +total_1
=======
now = arrow.now()
now1 = arrow.now()
now2 = arrow.now()

date = now.format('DD-YYYYMM')
date2 = now1.shift(days= -1).format('DD')
date3 = now2.shift(days= -1).format('DD-YYYYMM')
# print("{}{}".format(date,date2))

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
>>>>>>> 738a71b8f2bb3f8efb2e2c6edfdee8f50f1353df

print(total_1)
print (total_2)
print("--------<-Total 1")
print(total)
<<<<<<< HEAD
print("--------<-Total 2")
print(total_3)
=======
print("Palo Alto Geo Total")
print(ll6)
>>>>>>> 738a71b8f2bb3f8efb2e2c6edfdee8f50f1353df
