#Finnur Gauti Guðmundsson
#26.10.2021
#Æfingaverkefni-4

def brandari():
        print("Ha?.... ni tekinn og étinn")

def brandarar(nr):
    if nr ==2:
        print("Ha?.... ni ... á priki tekinn og étinn")
    elif nr ==2:
        print("Hæ ... na tekinn og étinn")
    elif nr ==3:
        print("Hæ ... na ... á priki tekinn og étinn")
    else:
        print("Þú ert mistök")

def hversKyns(kyn=""):
    if kyn == "kk":
        print("Karlmaður")
    elif kyn == "hvk":
        print("Kvennkyn")
    elif kyn == "kvk":
        print("Hvorukyn")
    elif kyn =="":
        print("Þekki ekki þetta kyn")
    else:
        print("Þú ert mistök")

def skrifaUt(listi):
    print(listi)
def stærsta(listi):
    stTala = 0

    for x in listi:
        if x > stTala:
            stTala = x 

    return stTala                
def minnsta(listi):
    minTala = stærsta(listi)

    for x in listi:
        if x < minTala:
            minTala = x 
    return minTala
def summa(listi):
    samtals=0
    for x in listi:
        samtals =samtals+x
    return samtals
def medaltal(listi):
    samtals = summa(listi)
    teljari = 0
    for x in listi:
        teljari +=1
    return samtals/teljari

def setning(nafn="Finnur",starf="KarlHóra", heima="Mótel í breiðholtinnu",aldur="17 en segist vera 22"):
    print(nafn,starf,heima,aldur)

def reiknaMedaltal(*tolur):
    medaltal = sum(tolur)/len(tolur)
    return round(medaltal,3)

def finnaOrd(texti, ordid):
    listi= texti.split(" ")
    fann =False
    for x in listi:
        if x ==ordid:
            print("Fann orðið sem leitað er að",x)
            fann = True
    if fann==False:
        print("Þetta orð er ekki í textanum")

on = True

while on == True:
    print("1. Brandari")
    print("2. Brandarar")
    print("3. Hverskyns")
    print("4. Tölur")
    print("5. Setning")
    print("6. Reikna meðaltal")
    print("7. Texti")
    print("8. Hætta")

    val = int(input("Hvað viltu gera:"))

    if val ==1:
        brandari()

    elif val ==2:
        nrBrandara = int(input("Veldu 1,2,3:"))
        brandarar(nrBrandara)       

    elif val ==3:
        hversKyns(input("Hvaða kyn ertu (kk, hvk, kvk:"))

    elif val ==4:
        
        listinn = []

        for x in range(5):
            tala = int(input("Komdu með tölu:"))
            listinn.append(tala)

        skrifaUt(listinn)
        print("Stærsta talann er:",stærsta(listinn))
        print("Minnsta talann er:",minnsta(listinn))
        print("Summa talnanna er:",summa(listinn))
        print("Meðaltal talnanna er:",medaltal(listinn))

    elif val ==5:
        setning()

    elif val ==6:
        print("Með 2 tölum:",reiknaMedaltal(2,69))

        print("Með 10 tölum",reiknaMedaltal(69,420,666,55,44,33,11,22,66,110))

    elif val ==7:
        textinn = input("Sláðu inn heila setningu:")
        leitAd= input("Hvaða orði ertu að leita að:")
        finnaOrd(textinn, leitAd)
        
    elif val ==8:
        on = False
