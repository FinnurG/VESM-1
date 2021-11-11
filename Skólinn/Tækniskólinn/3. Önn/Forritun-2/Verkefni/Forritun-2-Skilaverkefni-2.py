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
        pass
    
    #slökkva
    elif val ==3:
        on = False
    #ef rángt er valið í valmynd
    else:
        print("Þú valdir rangt")