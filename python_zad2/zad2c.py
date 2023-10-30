def parzyste(lista):
    wynik = []
    for liczba in lista:
        if liczba % 2 == 0:
            wynik.append(liczba)
    return wynik

lista1 = [2, 5, 7, 6, 11, 4, 22, 18,1,39]
wynik = parzyste(lista1)
print(wynik)



