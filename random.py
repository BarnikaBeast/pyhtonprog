import random

lista = []

#feltöltjük a listát random számokkal
for i in range(10): #10db szám lesz a listában
    lista.append(random.randint(1,100))
print(lista)


#feladat
#írjuk ki a 10 nél nagyobb számokat
for i in range(len(lista)):
    if lista[i] >=10:
        print(lista[i])
#írjuk ki a 10 nél kisebb számokat
print("*****************************")
for i in range(len(lista)):
    if lista[i] < 10:
        print(lista[i])


