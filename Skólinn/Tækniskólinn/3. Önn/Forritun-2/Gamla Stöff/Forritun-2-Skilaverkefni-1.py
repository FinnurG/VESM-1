# Finnur Gauti Guðmundsson
# 03.11.21
# Forritun-2-Skilaverkefni-1

import random

# Valmyndinn
on = True
while on == True:
    print("1. Random tölur")
    print("2. Skráning í áfanga")
    print("3. Teningakast")
    print("4. Celsíus Farenheit")
    print("5. Hraðatakmörk")
    print("6. Kveðja")
    print("7. Teningakast 2")
    print("8. Listar")
    print("99. Hætta")

    val = int(input("Veldu hvað þú vilt gera [1-8 og 99 til að hætta]:"))


    # Dæmi 1 Random tölur
    if val ==1:
        # Listinn & Teljararnir
        listinn = []
        tjlistinn = 1
        tjlistinnOfugt = 1
        tj1Til250 = 0
        tj251Til500 = 0

        # lykkja sem keyrir 70x
        for x in range(70):
            randomtala = random.randint(1, 500)
            listinn.append(randomtala)

            # Teljarinn fyrir 1-250 & 251-500
            if x < 251:
                tj1Til250 = tj1Til250 + 1

            elif x > 250:
                tj251Til500 = tj251Til500 + 1
        # Setja listann í dálka 4 hvern
        print("Teljarinn í dálka 4 hvern")
        for i in listinn:
            if tjlistinn % 4 ==0:
                 print(i)
            else:
                print(i, end=" ")
            tjlistinn = tjlistinn + 1

        # Gera gat þannig að það lookað flottara út og léttara að lesa
        print()

        print("Teljarinn öfugur í dálka 6 hvern")
        # Setja listann öfugann í dálka 6 hvern
        listinn.reverse()
        for i in listinn:
            if tjlistinnOfugt % 6 == 0:
                print(i)
            else:
                print(i, end=" ")
            tjlistinnOfugt = tjlistinnOfugt + 1


        # Gat aftur fyrir léttara að lesa
        print()


        print("Hægsta talann er:", (max(listinn)))
        print("Lægsta talann er:", (min(listinn)))



    # Dæmi 2 Skráning í áfanga
    elif val ==2:

        # Gera lista
        nafnHop = []

        # Fá hópfjölda og nafn
        fjHop = int(input("Hvað eru margir þátttakendur:"))
        # Fá nöfninn og aldur
        for x in range (fjHop):
            nafnMan = input("Nafn þátttakenda:")
            nafnHop.append(nafnMan)

        # Valmyndinn
        valMyndOn = True
        while valMyndOn ==True:
            print("1. Prenta nöfninn eftir stafrófsröð.")

            print("2. Eyða sér nafni.")
            print("3. Bæta við nafni.")
            print("4. Prenta óbreyttan lista.")
            print("99. Hætta")
            print()
            valMyndVal = int(input("Hvað viltu gera:"))

            if valMyndVal ==1:
                # Fá sortaðann lista
                for x in sorted(nafnHop):
                    print(x)
            elif valMyndVal ==2:
                # Fá nafn og eyða úr lista ef það er í listannum
                nafnEyda = input("Hvaða nafn viltu eyða:")
                for x in nafnHop:
                    if x == nafnEyda:
                        nafnHop.remove(x)
            elif valMyndVal ==3:
                # Fá nafn og bæta við lista
                nafnBaeta = input("Hvaða nafn viltu bæta við:")
                nafnHop.append(nafnBaeta)
            elif valMyndVal ==4:
                print("Óbreyttur listi er: ", nafnHop)

            elif valMyndVal ==4:
                pass
            elif valMyndVal ==99:
                valMyndOn = False



    # Dæmi 3 Teningakast
    elif val ==3:

        # Fá hversu oft
        teningakosttj = int(input("Hversu oft viltu kasta tveim teningum:"))
        teningakost = []

        # setja upp teljara
        talaOftast = 0
        talaMinnst = 0

        tala1 = 0
        tala2 = 0
        tala3 = 0
        tala4 = 0
        tala5 = 0
        tala6 = 0


        # Reikna út mjög mikið af því sama
        for x in range(teningakosttj):
            kast1 = random.randint(1, 6)
            kast2 = random.randint(1, 6)
            print("Teningur 1:", kast1)
            print("Teningur 2:", kast2)
            print("Samtal:", kast1+kast2)
            if kast1 == 1:
                tala1 = tala1 + 1
            elif kast1 == 2:
                tala2 = tala2 + 1
            elif kast1 == 3:
                tala3 = tala3 + 1
            elif kast1 == 4:
                tala4 = tala4 + 1
            elif kast1 == 5:
                tala5 = tala5 + 1
            elif kast1 == 6:
                tala6 = tala6 + 1

            if kast2 == 1:
                tala1 = tala1 + 1
            elif kast2 == 2:
                tala2 = tala2 + 1
            elif kast2 == 3:
                tala3 = tala3 + 1
            elif kast2 == 4:
                tala4 = tala4 + 1
            elif kast2 == 5:
                tala5 = tala5 + 1
            elif kast2 == 6:
                tala6 = tala6 + 1

        # Fá teljarana

        print("Talann 1 kom upp", tala1, "Sinnum")
        print("Talann 2 kom upp", tala2, "Sinnum")
        print("Talann 3 kom upp", tala3, "Sinnum")
        print("Talann 4 kom upp", tala4, "Sinnum")
        print("Talann 5 kom upp", tala5, "Sinnum")
        print("Talann 6 kom upp", tala6, "Sinnum")

        talaListi = [tala1, tala2, tala3, tala4, tala5, tala6]

        # Sjá hvaða tala kom mest upp

        if max(talaListi) ==tala1:
            talaOftast = 1
        if min(talaListi) ==tala1:
            talaMinnst = 1

        if max(talaListi) ==tala2:
            talaOftast = 2
        if min(talaListi) ==tala2:
            talaMinnst = 2

        if max(talaListi) ==tala3:
            talaOftast = 3
        if min(talaListi) ==tala3:
            talaMinnst = 3

        if max(talaListi) ==tala4:
            talaOftast = 4
        if min(talaListi) ==tala4:
            talaMinnst = 4

        if max(talaListi) ==tala5:
            talaOftast = 5
        if min(talaListi) ==tala5:
            talaMinnst = 5

        if max(talaListi) ==tala6:
            talaOftast = 6
        if min(talaListi) ==tala6:
            talaMinnst = 6

        # Prenta svarið

        print("Talann", talaOftast, "kom oftast upp")
        print("Talann", talaMinnst, "kom minnst upp")


    # Dæmi 4 Celsíus Farenheit
    elif val ==4:
        celedafar = int(input("Cel í far = 1. far í cel = 2"))
        if celedafar == 1:
            # Reikna celsius í farh eða öfugt svo returna útkomunni
            def celsius_i_farenheit(celsius):
                utkomac = (celsius*1.8)+32
                return utkomac
            celsius = float(input("Settu inn celsíus:"))
            print(celsius, "gráður celsíus eru", celsius_i_farenheit(celsius), "gráður farenheit.")
        elif celedafar == 2:

            def farenh_i_celsius(farenheit):
                utkomaf = (farenheit-32)/1.8
                return utkomaf
            farenheit = float(input("Settu inn farenheit:"))
            print(farenheit, "gráður farenheit eru =", farenh_i_celsius(farenheit), "gráður celsíus")
        else:
            print("Bara hægt að velja 1 eða 2")


    # Dæmi 5 Hraðatakmörk
    elif val ==5:

        def hversuHratt (hradi):
            # reikna refsistiginn og ef það eru 0 þá er ok annars refsistig
            refsistig = (hradi-90) // 5
            if refsistig < 1:
                texti = "Ókídókí"
            elif refsistig > 1:

                if refsistig > 12:
                    texti = "Þú missir ökuskírtenið"
                else:
                    texti = "Refsistig =", refsistig
            return texti
        hradi = int(input("Hversu hraður er bílinn"))
        print(hversuHratt(hradi))



    # Dæmi 6 Kveðja
    elif val ==6:
        def heilsa(nafn):
            # Finna hvort endinn er son, dóttir eða passar ekki
            if nafn[-3:] == "son":
                svar = "Sæll og blessaður", nafn
            elif nafn[-6:] == "dóttir":
                svar = "Sæl og blessuð", nafn
            else:
                svar = "Rángt nafn (þarf að enda á dóttir eða son)"
            return svar
        nafn = input("Komdu með fult nafn:")
        print(heilsa(nafn))

    # Dæmi 7 Teningakast 2
    elif val ==7:
        def kasta(hveOft):
            sum = 0
            for x in range(hveOft):
                # Fá teninga kastið og seta í summuna
                tala = random.randint(1, 6)
                sum = sum + tala
            return sum
        # ná í tölu frá notenda
        hveOft = int(input("Hve oft viltu kasta teningi:"))
        print("Summa allra kastanna er =", kasta(hveOft))

    # Dæmi 8  Listar
    elif val ==8:

        def eins(listi1, listi2, listi3):
            # Reikna út settinn
            return set(listi1) & set(listi2) & set(listi3)

        listi1 = [1, 8, 3, 5, 4, 10]
        listi2 = [1, 0, 7, 5, 71, 21, 13]
        listi3 = [1, 5, 6, 5, 8, 12, 3, 19]

        print("Allar tölurnar í listonum 3 =", eins(listi1, listi2, listi3))

    elif val ==99:
        # slökkva á
        on = False
    else:
        # ef notendi velur ekki rétta tölu
        print("Rangt valið.")