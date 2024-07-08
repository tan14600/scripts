import csv
def readFromBasic():
    with open('1.csv', 'r') as f:
        for lines in f:
            a = lines.split(',')
            # print(a[-1][-1])
            for i in a:
                print(i)  # for i in lines:

def readUsingLibrary():
    with open ('1.csv', 'r') as f:
        f1= list(csv.reader(f))
        for each in f1:
            print(each)

readUsingLibrary()

# 1. For each line you have 3 elements but it is a string which has comma has delimiter.
# 2. Ypu have to split the line using split func and then print each of the element.


