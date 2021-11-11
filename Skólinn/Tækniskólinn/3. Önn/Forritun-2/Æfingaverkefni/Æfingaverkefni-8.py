# Finnur Gauti Guðmundsson
# 05-11-21
# Æfingaverkefni-8 Skrá A

texti = input("Sláðu inn texta:")
skra = open("skraA.txt", "w")
skra.write(texti)
skra.close()
skra = open ("skraA.txt", "r")

print(skra.read())
skra.close()