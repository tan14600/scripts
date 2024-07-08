# Read the file into the python file
import json
import os
import subprocess

with open('repos-list.json', 'r') as file:
    data = json.load(file)


# Access the nested dicts in the list, and fetch the value of slug from every dict element.
# Add that to the "git clone" command 
# Access terminal and that folder where it should be cloned
# Run the above command in that terminal

directory = '/Users/tanmayirelangi/Desktop/Juspay/Repositories' 
os.chdir(directory)

for i in data:
    command = "git clone ssh://git@ssh.bitbucket.juspay.net/jbiz/"+i['slug']+".git"

    result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/zsh')
    print (result.stdout)   


    
