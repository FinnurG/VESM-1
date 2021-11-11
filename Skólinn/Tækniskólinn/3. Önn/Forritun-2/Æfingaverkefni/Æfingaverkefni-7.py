# Finnur Gauti Guðmundsson
# 04-11-21
# Æfingaverkefni-7 
import random

def prentaTuple(tup):
    print("prentaTuple")
    for x in tup:
        print(x, end=" ")
    print()
def paraRod(tup1, tup2):
    print("paraRöd")
    tj = 0 
    for x in tup1:
        print(tup1[tj], "og", tup2[tj])
        tj = tj+1
    print()
def paraRandom(tup1, tup2):
    print("paraRandom")
    for x in tup1:
        print(tup1[random.randint(0,5)], "og", tup2[random.randint(0,5)])
def paraRandomStakur(tup1, tup2):
    print("paraRandomStakur")
    nyrkk = list(tup1)
    nyrkvk = list(tup2)
    random.shuffle(nyrkk)
    random.shuffle(nyrkvk)
    tj = 0 
    for x in nyrkk:
        print(nyrkk[tj], "og", nyrkvk[tj])
        tj = tj+1
    print()
def finnaNafn(stafur,  tup):
    listi=[]
    for x in tup:
        if stafur in x:
            listi.append(x)
    if len(listi)>0:
        return listi
    else:
        return 0
def finnaN(t1, t2):
    listi= [x for x in t1 if x.count("n") > 1]
    listi2= [x for x in t2 if x.count("n") > 1]
    return listi+listi2

def finnaSima(dict,nafn):
    pass

on = True
while on ==True:
    print("1. Danspör")
    print("2. Símaskrá")
    print("3. Bekkur")
    print("99. Hætta")

    val = int(input("Hvaða valmynd viltu: "))

    if val ==1:
        kkTuple=("Finnur", "Guðmundur", "Dagur", "Einar", "Emil", "Gauti")
        kvkTuple=("Sara", "Gunnur", "Guðrún", "Gunnlaug", "Kristín", "Hrefna")

        prentaTuple(kkTuple)
        prentaTuple(kvkTuple)
        paraRod(kkTuple,kvkTuple)
        paraRandom(kkTuple,kvkTuple)
        paraRandomStakur(kkTuple, kvkTuple) 
        stafur = input("Komdu með staf:")
        print("Karlar með þennan staf:",finnaNafn(stafur, kkTuple),
              "Konur með þennan staf:", finnaNafn(stafur, kvkTuple))
        print("Nöfn með fleiri en eitt n", finnaN(kkTuple,kvkTuple))

    elif val ==2:
        myDict = {"Andri" : 8244328, 
                  "Helga" : 8495894,
                  "Rökkvi" : 6178123,
                  "Jónas" : 8948723,
                  "Hafdís" : 6911904,
                  "Metusalem" : 8236457,
                  "Guðmundur" : 8725864,
                  "Steinni" : 8659832,
                  "Erla" : 5812345,
                  "Sara" : 8926571}
        nafn = input("Komdu með nafn:")
        
    
    elif val ==3:
        pass

    elif val ==99:
        on = False

    else:
        print("Þú valdir rangt")