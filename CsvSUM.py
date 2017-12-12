#!/usr/bin/python3
import csv
import pandas as pd
import numpy as np
import arrow

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

print(total_1)
print (total_2)
print("--------<-Total 1")
print(total)
print("--------<-Total 2")
print(total_3)