# Finnur Gauti Guðmundsson
# 09-11-21
# Forritun-2-Skilaverkefni-2

#importa
import csv
import random

#setja upp def fyrir lið 1

#liður 1 def 1
def lesaSkra(nafncsv):
    #opna csv skjalið
    with open(nafncsv, "r", encoding="utf-8-sig" ) as lesari:
        
        texti = csv.reader(lesari,delimiter =";")
        spurn = list(texti)
    return spurn
#liður 1 def 2
def spurning(sp, sv):
    #fá gisk frá notenda
    gisk = input(sp)
    #ef gisk er rétt í fyrstu tilraun return True
    if gisk == sv:
        return True
    #ef gisk er ekki rétt í fyrstu tilraun
    else:
        #fá seinna gisk
        gisk = input(sp)
        #ef gisk er rétt í seinni tilraun return True
        if gisk == sv:
            return True
        #ef gisk er rángt bæði skiptin prenta rétta svarið   
        else:
            print("Þú giskaðir bæði skiptin rángt svarið er = ", sv)

#setja upp def fyrir lið 2

def skrifaIskra(listi,nafntxt):
    #opna csv skjalið og setja nýja línu
    with open(nafntxt, "a+", newline="", encoding="utf-8-sig") as lesari:
        #skrifa í csv skjalið það sem notendi vildi
        write = csv.writer(lesari,delimiter =";")
        #prennta csv skjalið
        write.writerow(listi)
        
def breytaUppl(simaskra,nafn,nyttGSM):
    pass
def eyda(simaskra,nafn):
    pass
def prenta():
    #opna csv skránna 
    with open("simaskra.csv", "r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        #prenta hverja línu í einu
        for row in csv_reader:
            print(row)

#setja valmynd upp
on = True

while on ==True:
    print("1. Spurningabanki")
    print("2. Símaskrá")
    print("3. Hætta")

    val = int(input("Hvaða valmynd viltu: "))

    #fyrri valmynd
    if val ==1:
        #lesa csv skjalið
        spurningar = lesaSkra("spurningar.csv")
        #stokka listanum
        random.shuffle(spurningar)
        #stigin
        stig = 0
        #for loopa fyrir listann
        for x in spurningar:
            #sækja svar hjá def-inu uppi
             if spurning(x[0], x[1]) == True:
                #reikna stiginn
                stig = stig+1
        #prenta stiginn        
        print("Þú hefur svarað", stig, "spurningum rétt")
    
    #seinni valmynd
    elif val ==2:
        kveikt = True
        while kveikt == True:
            valid = int(input("Veldu hvað þú vilt gera:"))
            if valid == 1:
                #búa til listann
                simaskrainputid = []
                #fá nafnið, kt og símanumerið frá notenda
                nafnid = input("Komdu með nafn:")
                kennitala = int(input("Komdu með kennitölu:"))
                simanumer = int(input("Komdu með símanúmer:"))
                #bæta nafninu, kt og símanúmerinu í listann
                simaskrainputid.append(nafnid)
                simaskrainputid.append(kennitala)
                simaskrainputid.append(simanumer)
                #kalla á skrifaIskra fallið með lista og csv skránni
                skrifaIskra(simaskrainputid,"simaskra.csv")

            elif valid == 2:
                #hef ekki tíma til þess að klára þetta en búinn með svona 50% af þessu
                with open("simaskra.csv", "r", encoding="utf-8-sig") as  file:
                    csv_reader = csv.reader(file)

                    lists_from_csv = []
                    for row in csv_reader:
                        lists_from_csv.append(row) 

                        validnafn = input("Hvaða notenda viltu breyta:")
                        validGSM = int(input("Nýja símanúmerið:"))
                        breytaUppl("simaskra.csv",validnafn,validGSM)

            # hef ekki tíma til að klára
            elif valid == 3:
                pass
            elif valid ==4:
                #kalla á prenta fallið
                prenta()
            elif valid ==5:
                kveikt = False
            else:
                print("Þú valdir rángt")
    #slökkva
    elif val ==3:
        on = False
    #ef rángt er valið í valmynd
    else:
        print("Þú valdir rangt")