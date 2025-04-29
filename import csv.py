import csv

# Open and read CSV file
with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    
    # Read header
    header = next(reader)
    print("Header:", header)

    # Read each row
    for row in reader:
        print(row)