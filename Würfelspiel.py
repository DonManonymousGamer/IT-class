import random
from gturtle import *
makeTurtle()
ht()
def wurfeln():
    return random.randint(1, 6)
#def wuerfchen():
    #print("idk")
def spiel():
    zufallszahl = random.randint(20, 40)
    anzahl_wurfel = int(input("Wie oft möchtest du würfeln? "))
    wurf_summe = 0
    count = 0
    for _ in range(anzahl_wurfel):
        input("Drücke eine beliebige Taste, um zu würfeln.")
        wurf = wurfeln()
        wurf_summe += wurf
        count = count + 1
        print(count, "Wurf:", wurf)
    differenz = abs(wurf_summe - zufallszahl)
    print("Die Summe der Würfelwürfe beträgt:", wurf_summe)
    print("Die Differenz zur Zufallszahl", zufallszahl, "beträgt:", differenz)

spiel()
