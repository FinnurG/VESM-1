# Finnur Gauti Guðmundsson
# 05-11-21
# Æfingaverkefni-9 Skrá B

on = True

while on ==True:
    print("1. Skrifa í skrá")
    print("2. Lesa úr skrá")
    print("99. Hætta")

    val = int(input("Hvaða valmynd viltu: "))

    if val ==1:
        skra = open("tolur.txt", "w")
        for x in range(5):
            tala = int(input("Sláðu inn tölu:"))
            skra.write(str(tala)+",")
        skra.close()
    elif val ==2:
        skra = open("tolur.txt", "r")
        innihald = skra.read().split(",")
        innihald.pop()
        innihald = list(map(int, innihald))
        medaltal = sum(innihald)/len(innihald)

        print(innihald)
        print("Meðaltal er =",medaltal)

        
        
    elif val ==99:
        on = False

    else:
        print("Þú valdir rangt")