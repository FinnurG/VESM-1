# Finnur Gauti Guðmundsson
# 13.04.21
# Forritun-2-Skilaverkefni-2

import csv

# Opna CSV fileið
with open('spurningar.csv', mode='r')as csv_file:
    pass

# lesa CSV fileið
csvFile = csv.reader(csv_file)

# displaying the contents of the CSV file
for lines in csvFile:
    print(lines)
