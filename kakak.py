# Lista adatszerkezet 
# lista indexei
# lista [] - > szögletes zárójel
# első elem [0]

lista = [] #ez egy üres lista
lista.append("Peugeot") #beírás a listába
lista.append("BMW") #beírás a listába
lista.append("Mercedes") #beírás a listába
lista.append("Lada Samara") #beírás a listába
lista.append("Fiat 500") #beírás a listába
lista.append("Toyota") #beírás a listába

print(lista)
for item in lista:
    print(item, sep=",")

print(len(lista)) #len függvény megadja a lista hosszát (hány darab elem van benne)

for i in range(len(lista)):
    print(lista[i])

# Feladat: Írasd ki hogy Szia 6 -szor!
for i in range(6):
    print("Szia!")

print("***************************************************")

lista2 = [1,2,3,4,5,6,7,8,9,10]
print(lista2)
for item in lista2:
    print(item)






