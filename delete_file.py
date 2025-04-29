import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt") 
else:
    raise Exception("Doesnt exist")