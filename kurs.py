wybór=input("Wprowadź nazwę owocu, który chcesz wyszukać: ")

owoce=["jabłko","pomarańcza","gruszka","banan",
"jabłko","truskawka","jabłko","jagoda"]

znaleziono=False

print("Lista została przeskanowana w poszukiwaniu: {}.".format(wybór))

for n, owoc in enumerate(owoce):
    if wybór==owoc:
        znaleziono=True
        if znaleziono==True:
            print("{} znajduje się na liście.".format(wybór)) 


print(bool(znaleziono))
