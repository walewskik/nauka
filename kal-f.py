from cmath import sqrt
import math


a=input("Wprowadź wartość b: ")
a=int(a)
b=input("Wprowadź wartość b: ")
b=int(b)
c=input("Wprowadź wartość c: ")
c=int(c)


delta=(b**2-4*a*c)
print("Delta jest równa:")
print(delta)


if  (delta)>0:
    print("Funkcja posiada dwa miejsca zerowe: ")
    x1 = ((-b-(math.sqrt(delta)))/(2*a))
    x2 = ((-b+(math.sqrt(delta)))/(2*a))
    print(x1,x2)
    
    
elif (delta)==0:
    print("Funkcja posiada jedno miejsce zerowe:")
    x0= ((-b-(math.sqrt(delta)))/2)
    print(x0)
else:
    print("Funkcja nie posiada żadnych miejsc zerowch.")

p=(-b/(2*a))
q=(-(delta)/(4*a))
W = (p,q)
print("Wierzchołek ma współrzędne:")
print(W)





