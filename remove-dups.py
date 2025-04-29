
import os
import subprocess

#Read the CSV file
with open('sample.csv', 'r') as file:
    content = file.read()
flag=0
a=''
#Add the CSV contents to a list, and use set DS on it to remove duplicates
for i in content:
    if i == ',':
        print(i,end='\n')
        flag=0
    elif i == "'" and flag==13:
        print(a)
    else:
        flag+=1
        a=a+i
        print(a)

