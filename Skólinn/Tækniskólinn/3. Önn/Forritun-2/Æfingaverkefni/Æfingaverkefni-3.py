# Finnur Gauti Guðmundsson
# 20.10.21
# Forritun-2-Æfingaverkefni-3

# Valmyndinn
on = True

import math
import datetime

while on == True:
    print("1. Þrjár tölur")
    print("2. Aldarmót")
    print("3. Tölur")
    print("4. Yfirflatsmál og rúmmál")
    print("5. lykilorð")
    print("6. Texti")
    print("7. Samnefnari")
    print("99. Hætta")

    val = int(input("Veldu hvað þú vilt gera:"))

    if val ==1:
        
        tala1 = int(input("Komdu með fyrstu tölu:"))
        tala2 = int(input("Komdu með seinni tölu:"))
        tala3 = int(input("Komdu með þriðju tölu:"))

        minstaT = min(tala1,tala2,tala3)
        staerstaT = min(tala1,tala2,tala3)
        if tala1 == tala2 & tala3:
            print("Allar tölur eru jafn stórar")
        else: 
            print("Minsta talann er:", minstaT, "og stærsta talan er:", staerstaT) 

    elif val ==2:
        now = datetime.datetime.now()
        
        nafn = (input("Hvað heitir þú:"))
        aldur = int(input("Hvað ert þú gamall/ur:"))
        afmaeliAr = int(input("Ert þú búin/n að eiga afmæli á árinu? 1 = Já 2 = Nei:"))

        ar = now.year

        if afmaeliAr == 1:
            print("Þú verður", (2100-ar)+aldur -1, "næstu aldarmot")
        elif afmaeliAr == 2:
                        print(nafn,"Þú verður", (2100-ar)+aldur, "næstu aldarmot")
        else:
            print("Rángt valið")
        
    elif val ==3:
        
        tala = 1
        summa = []
    
        while tala !=0:
            tala = int(input("Komdu með tölu:"))
            if tala !=0:
                summa.append(tala)
            
        print("Summa talanna er:", sum(summa))
        print("Fjöldi talna sem lsegin var inn:", len(summa))
        print("Meðaltal talnanna er:", sum(summa) / len(summa))

    elif val ==4:
        
        radius = float(input("Hvað er radíus kúlurnar:"))

        print("Rúmmál kulurnar er:", round((4.0*radius**3*math.pi)/3, 3))
        print("Yfirborðsflatarmál kúlunnar er:", round(4*math.pi*radius**2, 3))

    elif val ==5:
        lykilord = input("Sláðu inn allavega sex tákna lykilorð með blöndu af tölustöfum og bókstöfum:")
        if len(lykilord)<6:
            print("Lykilorð er ekki nógu langt")
        else:
            erBokstafur=False
            erTolustafur=False

            for x in lykilord:
                if x.isdigit():
                    erTolustafur=True
                if x.isalpha():
                    erBokstafur=True
            if erBokstafur and erTolustafur:
                print("Flott lykiorð")
            else:
                print("Þetta lykilorð er vitlaust")    

    elif val ==6:
        texti = input("Sláðu inn texta")
        fjH=0
        fjL=0

        for x in texti:
            if x.isupper():
                fjH=fjH+1
            if x.islower():
                fjL=fjL+1
        print("Fjöldi hástafa er:", fjH, "Fjöldi lágstafa er:", fjL)
        
    elif val ==7:
        tala1 = int(input("Fyrri Tala:"))
        tala2 = int(input("Seinni Tala:"))

        samnefnari = 0



        for x in range(1,tala2+2):
            if tala1 % x==0 and tala2 % x==0:
                samnefnari = x
        
        print("Hæsti samnefnari er", samnefnari)

    elif val ==99:
        on = False
    
    else:
        print("Rángt valið.")