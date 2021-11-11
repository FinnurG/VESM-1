# Finnur Gauti Guðmundsson
# 20.10.21
# Forritun-2-Æfingaverkefni-2

# Valmyndinn
on = True

while on == True:
    print("1. Fornöfn")
    print("2. Ekrar í fermetra")
    print("3. Breidd")
    print("4. Framhaldsskóli")
    print("5. Prósentur")
    print("99. Hætta")

    val = int(input("Veldu hvað þú vilt gera:"))

    if val ==1:
        nafn1 = input("Fyrra nafn:")
        haed1 = int(input("Hæð í sentimetrum:"))
        nafn2 = input("Seinna nafn:")
        haed2 = int(input("Hæð í sentimetrum:"))

        if haed1 > haed2:
            print(nafn1, "er stærri en", nafn2)

        elif haed1 < haed2:
            print(nafn2, "er stærri en", nafn1)

        elif haed1 == haed2:
            print(nafn1, "og", nafn2, "eru jafn há")

        else:
            print("Vittlaust sett inn:")

    elif val ==2:
        
        lengd = float(input("Lengdinn:"))
        breidd = float(input("Breiddin:"))
        
        ekrar = (lengd*breidd)/4046

        print("Þessi reitur er:", round(ekrar,4), "ekrar")

    elif val ==3:
        
        breidd = int(input("Breidd fernings í metrum:"))
        teljari = 10
        print("Stærð   Lengd í ekrum")
        for x in range(10,201,10):
            svar = (x * breidd)/4046
            print(teljari,"   ", round(svar,7))
            
            teljari = teljari + 10

    elif val ==4:

        skamm = input("Skammstöfu áfanga 3 hástafir og 4 tölustafir:")
        b_OK= False
        t_OK= False
        
        bok = skamm[:3]
        tol = skamm[3:]

        if bok.isupper() and bok.isalpha():
            b_OK = True

        if tol.isdigit() and len(tol)==4:
            t_OK = True

        if b_OK and t_OK:
            print("Flott áfanganúmer")

        else:
            print("Rángt sláð inn")

    elif val ==5:
        heild = int(input("Hver er heildin:"))
        prosent = int(input("Hver er prósentinn:"))

        nidurstada = (prosent/100) * heild

        print("Niðurstaðan:", nidurstada)

    elif val ==99:
        on = False
    
    else:
        print("Rángt valið.")