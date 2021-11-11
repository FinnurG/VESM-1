# Finnur Gauti Guðmundsson
# 12.04.21
# Forritun-2-Tímaverkefni-1

import random

on = True
while on == True:
    print("1. Fall með randomlista")
    print("2. Strengjaföll")
    print("3. Dictionary")
    print("4. Hætta")

    val = int(input("Veldu hvað þú vilt gera [1-4]:"))

    # Liður 1. Fall með randomlista
    if val ==1:
        rlisti = []
        rlistiAn15 = []
        rlistiAn12 = []
        def randomListi(fjListi, randbyrjun, randendir):
            for x in range(fjListi):
                randomTala = rlisti.append(random.randint(randbyrjun, randendir))
            print(rlisti)
        randomListi(20, 10, 20)
        for x in rlisti:
            if x != 15:
                rlistiAn15.append(x)
        print("Listi án 15:", rlistiAn15)
        for x in rlisti:
            if x == 12:
                rlistiAn12.append(22)
            else:
                rlistiAn12.append(x)
        print("Listi þar se 12 er breytt í 22:", rlistiAn12)


    # Liður 2. Strengjaföll
    elif val ==2:
        def fjoldiOrda(setning):
            svar = len(setning.split())
            return print("Fjöldi orða í þessari setningu eru: " + str(svar))
        fjoldiOrda(input("Komdu með setningu:"))

        def skammstofun(setning):
            setning_split = setning.split()
            skammstofuninn = ""
            for x in setning_split:
                skammstofuninn = skammstofuninn + x[0].upper()

            return print("Skammstöfun allra orðanna er:", skammstofuninn)
        skammstofun(input("Komdu með setningu:"))
    # Liður 3. Dictionary
    elif val ==3:
        """
        
        Skil ekki hvernig ég á að gera þetta og tíminn er búinn.
        
        hvolpar = {'Labrador': 350000, 'Husky': 400000, 'Poodle': 300000, 'Sheffer': 350000, 'Doberman': 300000}

        valm = True
        while valm ==True:
            print("A. Breyta verði")
            print("B. Bæta inn staki (Tegund og upphæð)")
            print("C. Eyða staki (Tegund og upphæð)")
            print("D. Prenta út tegund og upphæð dýrasta hvolps")
            print("E. Prenta út heildar söluverð allra hvolpanna")
            print("F. Hætta")

            valid = input("Hvað vilt þú gera:")

            if valid =="A":
                pass
            elif valid =="B":
                pass
            elif valid =="C":
                pass
            elif valid =="D":
                pass
            elif valid =="E":
                pass
            elif valid =="F":
                valm = False
        """

    # 4.Hætta
    elif val ==4:
        on = False
    else:
        print("Rángt valið bara 1-4")
