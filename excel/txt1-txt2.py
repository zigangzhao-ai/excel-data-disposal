import xlwt
import codecs

with open('001.txt') as f:
    read_data=f.read()
    a=read_data.split()
    print(a)
with open("002.txt","w") as f1:
    for x in a:
        f1.writelines('\n'+str(x))
    f1.close()