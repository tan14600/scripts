import csv
import os
import subprocess

# Read the CSV file and extract 'slug' values
with open('ms-repos.csv', 'r') as file:
    reader = csv.DictReader(file)
    slugs = [row['slug'] for row in reader]

# Change to the target directory
directory = '/Users/tanmayirelangi/Desktop/Juspay/Repositories'
os.chdir(directory)

# Run the git clone command for each slug
for slug in slugs:
    command = f"git clone ssh://git@ssh.bitbucket.juspay.net/jbiz/{slug}.git"
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/zsh')
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
