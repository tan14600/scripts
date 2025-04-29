f = open("demoFile.txt", "r")

# Modes: a- append; r-read(default); w- write; x-create
# Filecontent: t- text (default); b- binary [Eg: images]

for x in f:
    for y in x:
        if y is 'l':
            continue
        else:
            print(y, end='-')

f.close()
