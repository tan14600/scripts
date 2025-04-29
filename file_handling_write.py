f = open("myfile.txt", "x")
f.write("abc")
f.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()