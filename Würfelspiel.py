import random
from gturtle import *
makeTurtle()
ht()
print("Le Würfelspiel")
Zielnummer=(random.randrange(20, 40))
print(Zielnummer)
wuerfeln = input("Welches Key willst du zum Würfeln benutzen?")
Frage = inputInt("Wie oft willst du würfeln?")
zahl=0
def wuerfchen():
    zahl=zahl+1
    print(zahl, "Wurf ist:")
    

Screen().onkey(wuerfeln, wuerfchen)
Screen().listen()