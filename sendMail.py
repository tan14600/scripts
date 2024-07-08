import requests
import csv

with open ('1.csv', 'r') as file:
    f = csv.reader(file)
    for each in f:

