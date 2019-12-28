"""
import pandas as pd

data = pd.read_table(r"002.txt",sep=',',header=None)

data.to_csv('002.csv',index=None, header=None)
"""

import xlwt
hr_book= xlwt.Workbook(encoding='ascii')
hr_sheet=hr_book.add_sheet('HR_title',cell_overwrite_ok=True) 

with open(r'002.txt','r+') as title:
    hrtitle = title.read()    
    hrtitle_list= hrtitle.split() 
    print(hrtitle_list)
   
i=0
j=0
for hl in hrtitle_list:    
    
    hr_sheet.write(i,j,hl)      
    i=i+1 
hr_book.save('002.xls')             