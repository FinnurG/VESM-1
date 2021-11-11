# Finnur Gauti Guðmundsson
# 09-11-21
# Forritun-2-Skilaverkefni-2

import csv
import random

def lesaSkra(nafncsv):
    with open(nafncsv, "r") as lesari:
        texti = csv.reader(lesari,delimiter =";")
        spurn = list(texti)
    return spurn
def spurning(spurningSvar):
    pass

on = True

while on ==True:
    print("1. Spurningabanki")
    print("2. Símaskrá")
    print("3. Hætta")

    val = int(input("Hvaða valmynd viltu: "))
    
    if val ==1:
        spurningar = lesaSkra("spurningar.csv")
        for x in spurningar:
            print(x)
        
    
    elif val ==2:
        pass
    
    elif val ==3:
        on = False

    else:
        print("Þú valdir rangt")