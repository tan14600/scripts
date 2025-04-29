#You are given a list containing both integers and floats. Write a Python program that iterates over the list and prints only the integer values. 

n = [1, 2.0, -3, 4, 5.0, -6] 
for i in n:
    if type(i) == int and i>0:
        print(i)

