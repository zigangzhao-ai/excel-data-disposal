#coding=utf-8
import xlrd
import os
import numpy as np
file_path = r'001.xlsx'
#file_path = file_path.decode('utf-8')

data = xlrd.open_workbook(file_path)

#print(data)


table = data.sheet_by_name('Sheet1')
nrows = table.nrows
print(nrows)
ncols = table.ncols


###write_to _txt
f = open("001.txt","w")
for i in range(0,nrows):

   rowvalue = table.row_values(i)
   #print(rowvalue)

   for x in rowvalue:
       f.writelines('\n'+str(x))
f.close()


