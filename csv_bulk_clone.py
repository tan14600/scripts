import os
import subprocess

# Read the CSV file and extract the 'slug' values
with open('infra_repos.csv', 'r') as file:
# with open('ms-repos.csv', 'r') as file:
    content = file.read()

# Split the content by comma to get the list of slugs
slugs = content.strip().split(',')

# Remove any empty strings from the list (e.g., due to trailing commas)
slugs = [slug for slug in slugs if slug]

# Change directory to the desired folder
directory = '/Users/tanmayi.relangi/Desktop/Juspay/Repositories/Infra'
os.chdir(directory)

# Construct and execute the 'git clone' command for each slug
for slug in slugs:
    command = f"git clone ssh://git@ssh.bitbucket.juspay.net/infra/{slug}.git"
    print(f"Executing command: {command}")  # Print the command being executed
    result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/zsh')
    
    # Print stdout and stderr for debugging
    print("Standard Output:\n", result.stdout)
    print("Standard Error:\n", result.stderr)
    
    # Check if the command was successful
    if result.returncode == 0:
        print(f"Successfully cloned {slug}\n")
    else:
        print(f"Failed to clone {slug}\n")

# Print a summary at the end
print("Script execution completed.")
