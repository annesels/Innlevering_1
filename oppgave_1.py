import math

#a = float(input("Antall H+-ioner i mol per liter "))
#print("Du skrev inn tallet",a)

a = 10**(-7)

ph = -(math.log10(a))
print("Ph verdien din er",ph)
if 0 <= ph and 7 > ph:
    print("Løsningen er sur")
elif 7 == ph:
    print("Løsningen er nøytral")
elif 7 < ph and 14 >= ph:
    print("Løsningen er basisk")
