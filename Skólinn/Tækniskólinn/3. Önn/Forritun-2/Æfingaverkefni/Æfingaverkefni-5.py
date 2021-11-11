# Finnur Gauti Guðmundsson
# 03-11-21
# Æfingaverkefni-5 List comprehension

import random
import math

on = True

while on ==True:
    print("1. 10-20")
    print("2. 1-1000")
    print("3. 100x 200-800")
    print("4. Nafnalisti")
    print("5. Eigin val")
    print("99. Hætta")

    val = int(input("Hvaða valmynd viltu: "))

    if val ==1:
        tridjaveldi = [3**x for x in range(10,20)]
        print(tridjaveldi)

    elif val == 2:
        listi = [x for x in range(1,1000) if x % 5 == 0 and x % 2 == 1]
        print(listi) 
    
    elif val ==3:   
        
        randomlisti =[random.randint(200,800) for x in range(100)]
        
        medFjor = [x for x in randomlisti if str(x)[-1] =="4"]

        print(randomlisti)
        print(medFjor)

    elif val == 4:
        kk = ["kalli", "jón", "halli", "jónas", "andri"]
        kvk = ["rósa", "sara", "jóna", "sandra", "guðrún"]
        danslisti=[x +"dansar við" +y for x in kk for y in kvk]
        print(danslisti)
    
    elif val ==5:
        annadveldi = [2**x for x in range(69,420)]
        print(annadveldi)

    elif val ==99:
        on = False

    else:
        print("Þú valdir rangt")