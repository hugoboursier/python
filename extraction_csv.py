import csv

file = open("res/equipements.csv","r")
test = csv.reader(file)
for row in test:
    if row[1]=="Geneston": print(row[3])