import random
from gturtle import *
makeTurtle()
ht()
print("Le Würfelspiel")
Zielnummer=(random.randrange(20, 40))
print(Zielnummer)
Frage = inputInt("Wie oft willst du würfeln?")
zahl=0
def wuerfchen():
    global zahl
    zahl= zahl+1
    if (zahl == Frage):
        print(zahl, "Wurf ist:")
        print("finished")
    elif(zahl >= Frage):
        return
    else:
        print(zahl, "Wurf ist:")
Screen().onkey(wuerfchen, 'Enter')
Screen().listen()
