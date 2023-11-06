# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
#następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
#Operatory arytmetyczne, logiczne i typowanie 3
#uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
#wyświetlić ( print )


def create_greeting(name, surname):
    greeting = f"Cześć {name} {surname}!"
    return greeting

name = "John"
surname= "Deer"
result = create_greeting(name, surname)
print(result)


#Stworzyć funkcję, która przyjmie 2 argumenty typu int , a następnie zwróci wynik
#mnożenia obu liczb.

def pomnoz(a, b):
    return a * b

# Przykładowe użycie funkcji
liczba1 = 5
liczba2 = 3
wynik = pomnoz(liczba1, liczba2)
print(wynik)

#Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
#parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
#uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
#wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
#"Liczba nieparzysta"

def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

# Przykładowe użycie funkcji
liczba = 7
wynik = czy_parzysta(liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

#Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
#pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
#jako typ logiczny bool

def sprawdz_suma(a, b, c):
    return a + b >= c

# Przykładowe użycie funkcji
liczba1 = 5
liczba2 = 3
liczba3 = 8

wynik = sprawdz_suma(liczba1, liczba2, liczba3)

if wynik:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej.")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza niż trzecia.")



#Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int
# Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z parametru
#pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.


def sprawdz_wartosc_w_liscie(lista, wartosc):
    return wartosc in lista

# Przykładowe użycie funkcji
moja_lista = [1, 2, 3, 4, 5]
szukana_wartosc = 3

wynik = sprawdz_wartosc_w_liscie(moja_lista, szukana_wartosc)

if wynik:
    print(f"Lista zawiera wartość {szukana_wartosc}.")
else:
    print(f"Lista nie zawiera wartości {szukana_wartosc}.")



#Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
#Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
#element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.

def przetworz_listy(lista1, lista2):

    polaczona_lista = lista1 + lista2

    unikalna_lista = list(set(polaczona_lista))

    przetworzona_lista = [x**3 for x in unikalna_lista]
    
    return przetworzona_lista

# Przykładowe użycie funkcji
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

wynik = przetworz_listy(lista1, lista2)
print(wynik)












 