import xlwt
import codecs

with open('001.txt') as f:
    read_data=f.read()
    a=read_data.split()
    print(a)

j = 0
for x in a:
    if len(x)==0:
        j+=1
print("=======================")

print(j)

print("=======================")


i = 0
b = []
for x in a:
    i = i + 1
    #print(type(x))
    
    if len(x)==1 and len(a[i])==1 and len(a[i+1])!=1:
        x1 = x + a[i]
        b.append(x1)
        print(x1)
    if len(x)>=3:
        b.append(x)
#print(b)      
print(j)  
"""
with open("002.txt","w") as f1:
    for x in a:
        f1.writelines('\n'+str(x))
    f1.close()
"""