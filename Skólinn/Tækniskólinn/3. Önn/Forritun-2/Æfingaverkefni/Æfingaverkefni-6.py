# Finnur Gauti Guðmundsson
# 03-11-21
# Æfingaverkefni-6 Létt Dictonary Æfing

on = True

while on ==True:
    print("1. Búa til dictionary")
    print("2. Prenta dictionary")
    print("3. Eyða lit")
    print("4. Prenta ákveðin lit")
    print("5. Sýna notkun fallanna")
    print("99. Hætta")

    val = int(input("Hvaða valmynd viltu: "))

    if val ==1:
        litadicct={1:"Gulur",2:"Rauður",3:"Grænn",4:"Brúnn",5:"Appelsínugulur",6:"Grár",7:"Hvítur",8:"Blár",9:"Fjólublár",10:"Svartur"}


    
    elif val ==2:
        for x in litadicct:
            print(x, " -> ",litadicct[x])
    
    elif val ==3:
        
        for x in litadicct:
            print(x, " -> ",litadicct[x])
        valid = int(input("Veldu einn lit til að eyða og prenta:"))
        print(litadicct.pop(valid))


    elif val ==4:
        for x in litadicct:
            print(x, " -> ",litadicct[x])
        valid = int(input("Veldu einn lit til að prenta:"))
        print(litadicct.get(valid))
    
    elif val ==5:
        
        print("Obreyttur = ",litadicct)
        print("items = ",litadicct.items())
        print("keys = ",litadicct.keys())
        print("values = ",litadicct.values())
        print("Nú er búið að eyða öllu út úr dictonary ",litadicct.clear())

    elif val ==99:
        on = False

    else:
        print("Þú valdir rangt")