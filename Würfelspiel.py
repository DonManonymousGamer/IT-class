import random
from gturtle import *
makeTurtle()
ht()
screen = Screen()

wurf_summe, differenz, zufallszahl, count = 0, 0, 0, 0

def idk_random():
    global wurf_summe
    global count
    
    wurf = random.randint(1, 6)
    wurf_summe += wurf
    count = count + 1
    print(count, "Wurf:", wurf)
    print("Drücken Sie die Eingabetaste für die nächste.")
    
def spiel():
    global differenz
    global wurf_summe
    global zufallszahl
    global count
    
    zufallszahl = random.randint(20, 40)
    print("Zielnummer ist:", zufallszahl)
    anzahl_wurfel = int(input("Wie oft möchtest du würfeln? "))


    screen.onkey(idk_random, "enter")
    screen.listen()
    
    while True:
        if (anzahl_wurfel <= count):
            differenz = abs(wurf_summe - zufallszahl)
            print("Die Summe deiner Würfe war:", wurf_summe)
            print("Ihre Differenz zu", zufallszahl, "beträgt:", differenz)
            break
            
    screen.bye()
    

spiel()

