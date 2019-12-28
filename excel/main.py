#coding=utf-8
import xlrd
import os
import xlwt
import codecs
import numpy as np
file_path = r'001.xlsx'
#file_path = file_path.decode('utf-8')

data = xlrd.open_workbook(file_path)

#print(data)


table = data.sheet_by_name('Sheet1')
nrows = table.nrows
print(nrows)
ncols = table.ncols


###excel-write_to _txt
f = open("001.txt","w")
for i in range(0,nrows):

   rowvalue = table.row_values(i)
   #print(rowvalue)

   for x in rowvalue:
       f.writelines('\n'+str(x))
f.close()


###delete-blank
with open('001.txt') as f1:
    read_data=f1.read()
    a=read_data.split()
    #print(a)

i = 0
b = []
for x in a:
    i = i + 1
    #print(type(x))
    
    if len(x)==1 and len(a[i])==1 and len(a[i+1])>=3:
        x1 = x + a[i]
        b.append(x1)
        print(x1)
    if len(x)==1 and len(a[i])==1 and len(a[i+1])==1 and len(a[i+2])==1:
        x2 = x + a[i]
        b.append(x2)
    if len(x)>=3:
        b.append(x)
#print(b)
print(len(b))

j=0   #len(t)==len(b[j]) and 
for x in b:
    j=j+1
    if len(x)== 2 and len(b[j])==2 and len(b[j+1])==2:         
        x3 = b[j]
        b.remove(x3)    
#print(b)
print(len(b))

##rewrite-to-txt
with open("002.txt","w") as f2:
    for x in b:
        f2.writelines('\n'+str(x))
    f2.close()
 
##txt-excel
hr_book= xlwt.Workbook(encoding='ascii')
hr_sheet=hr_book.add_sheet('HR_title',cell_overwrite_ok=True) 

with open(r'002.txt','r+') as title:
    hrtitle = title.read()    
    hrtitle_list= hrtitle.split() 
    print(len(hrtitle_list))
   
i=0
j=0
for hl in hrtitle_list:    
    
    hr_sheet.write(i,j,hl)      
    i=i+1 
hr_book.save('002.xls')   