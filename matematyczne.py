#komentarz
import moduly.walidator
# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
def pole_kola():
    r = input('Podaj dlugosc promienia kola w centymetrach ')
    if moduly.walidator.walidacja(r) == True:
        wzor = 3.14 * float(r)**2
        print(f'Pole kola o zadanym promieniu to {wzor}')

# 7. Napisz program do rozpoznawania czy podana liczba jest parzysta czy nie.
def parzysta():
    number = input('Podaj liczbę całkowitą ')
    if moduly.walidator.walidacja(number) == True:
        if (int(number) % 2 == 0):
            print(f'Podana liczba jest parzysta')
        else:
            print(f'Podana liczba jest nieparzysta')

# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
def dziel_lub():
    a = input('Podaj liczbę ')
    if moduly.walidator.walidacja(a) == True:
        if (float(a) % 3 == 0) or (float(a) % 5 == 0) or (float(a) % 7 == 0):
            print('Liczba jest podzielna przez 3 lub 5 lub 7')
        else:
            print('Liczba nie dzieli się przez 3, 5, 7')

# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
def dziel_i():
    a = input('Podaj liczbę ')
    if moduly.walidator.walidacja(a) == True:
        if (float(a) % 3 == 0) and (float(a) % 5 == 0) and (float(a) % 7 == 0):
            print('Liczba jest podzielna przez 3 i 5 i 7')
        else:
            print('Liczba nie dzieli się przez 3 i 5 i 7')
# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
def digit():
    number = input('Podaj liczbę ')
    if moduly.walidator.walidacja(number) == True:
        liczba = float(number)
        print(f'Pierwsza cyfra to {number[0]}')
        print(f'Ostatnia cyfra to {number[-1]}')

# 6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
def przeliczenie():
    bn = input('Podaj liczbę w formacie binarnym ')
    if moduly.walidator.walidacja(bn) == True:
        wzor = (int(bn[0])*2**5)+(int(bn[1])*2**4)+(int(bn[2])*2**3)+(int(bn[3])*2**2)+(int(bn[4])*2**1)+(int(bn[5])*2**0)
        print(f'Podana liczba w systemie dziesiętnym to {wzor}')


