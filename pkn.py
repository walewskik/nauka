from operator import truediv
import getpass

poprawne_opcje=["kamień","papier","nożyce"]
w_gracza1=0
w_gracza2=0

while w_gracza1<3 and w_gracza2<3:
    wybór_gracza_poprawny=True

    while wybór_gracza_poprawny:
        wybór_gracza1=getpass.getpass("Wybór Gracza1: ")
        if wybór_gracza1 in (poprawne_opcje):
            wybór_gracza_poprawny=False
        else: print("Proszę wprowadzić poprawną opcję.")
    
    wybór_gracza_poprawny=True
    while wybór_gracza_poprawny:
        wybór_gracza2=input("Wybór Gracza2: ")
        if wybór_gracza2 in (poprawne_opcje):
            wybór_gracza_poprawny=False
        else:
            print("Proszę wprowadzić poprawną opcję.")

    if wybór_gracza1 == "papier" and wybór_gracza2== "kamień" or\
    (wybór_gracza1)=="kamień" and wybór_gracza2=="nożyce" or\
    (wybór_gracza1)=="nożyce" and wybór_gracza2=="papier":
        print("Gracz 1 wygrał.")
        w_gracza1=w_gracza1+1

    elif wybór_gracza1==wybór_gracza2:
        print("Remis.")
    else:
        print("Gracz 2 wygrał")
        w_gracza2=w_gracza2+1

if w_gracza1==3:
    print("Gracz1 wygrał.")
    if w_gracza1==3 and w_gracza2==0:
        print("Gracz1 wygrał 3:0.")
    elif w_gracza1==3 and w_gracza2==1:
        print("Gracz1 wygrał 3:1.")
    elif w_gracza1==3 and w_gracza2==2:
        print("Gracz1 wygrał 3:2.")

elif w_gracza2==3:
    print("Gracz2 wygrał.")
    if w_gracza2==3 and w_gracza1==0:
        print("Gracz2 wygrał 3:0.")
    elif w_gracza2==3 and w_gracza1==1:
        print("Gracz2 wygrał 3:1.")
    elif w_gracza2==3 and w_gracza1==2:
        print("Gracz2 wygrał 3:2.")