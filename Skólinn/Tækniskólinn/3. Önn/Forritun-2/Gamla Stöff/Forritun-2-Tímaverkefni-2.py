# Finnur Gauti Guðmundsson
# 05.05.21
# Forritun-2-Tímaverkefni-2

import random
import csv

on = True
while on == True:
    print("1. Randomtölur")
    print("2. Skráarvinnsla")
    print("3. Klassin Þríhyrningur")
    print("4. Hætta")

    val = int(input("Veldu hvað þú vilt gera:"))

    if val ==1:

        def gera_lista(byrjun,endir,fjoldi):
            lista = [random.randrange(byrjun,endir) for i in range(fjoldi)]
            return lista

        def syna_lista(listi):
            tj = 1
            for x in gera_lista(5, 15, 8):
                if tj < len(listi):
                    print(x,end=":")
                    tj = tj + 1
                else:
                    print(x)
        syna_lista(listi=gera_lista(5, 15, 8))

        def medaltal():
            random_tolur = [random.randint(1,10) for i in range(100)]
            return print("Meðal tal þessum tölum er =",format(sum(random_tolur) / len(random_tolur), ".4f"))
        medaltal()

    elif val ==2:
        with open("nemendur.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                print(row)


    elif val ==3:
        pass
        #skil ekki neitt í þessu
    elif val ==4:
        on = False