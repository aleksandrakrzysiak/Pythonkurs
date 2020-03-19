# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
# temperature = input ('Podaj ilosc stopni Celsjusza ')
# if temperature.isnumeric():
#     def c_t_f(temperature):
#         wzor = 32 + 9/5 * float(temperature)
#         return wzor
#     wynik = c_t_f(temperature)
#     print (f'Ilosc stopni Fahrenheita to {wynik}')
# else:
#     print('Podana wartosc nie jest wartością liczbową')

# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
# temperature = input ('Podaj ilosc stopni Fahrenheita ')
# if temperature.isnumeric():
#     def f_t_c(temperature):
#         wzor = 5/9*(float(temperature)-32)
#         return wzor
#     wynik = f_t_c(temperature)
#     print (f'Ilosc stopni Fahrenheita to {wynik}')
# else:
#     print('Podana wartosc nie jest wartością liczbową')

# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
# def pole_kola(promien):
#     wzor = 3.14 * float(promien)**2
#     return wzor
#
#
# r = input ('Podaj dlugosc promienia kola w centymetrach ')
# if r.isnumeric():
#     print(f'Pole kola o zadanym promieniu to {pole_kola(r)}')
# else:
#     print('Podana wartość nie jest wartością liczbową')


# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
# def digit(a):
#     liczba = a
#     return liczba
#
#
# number = input('Podaj liczbę ')
# if number.isnumeric():
#     print(f'Pierwsza cyfra to {digit(number[0])}')
#     print(f'Ostatnia cyfra to {digit(number[-1])}')
# else:
#     print('Podana wartość nie jest wartością liczbową')

# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +-------+
#     |       |
#     |       |
#     +-------+

# wysokosc = int(input ('Podaj wysokość prostokąta '))
# szerokosc = int(input ('Podaj szerokość prostokąta '))
# poczatek_koniec = '+' + szerokosc * '-' + '+'
# srodek = '|'+(' '* szerokosc ) + '|' + '\n'
# print (poczatek_koniec)
# print (wysokosc *srodek, end=' ')
# print (poczatek_koniec)

def prostokat(x,y):
    for i in range(x):
        print('+' + x * '-' + '+')
        print(y*'|'+(' '* x ) + '|' + '\n')
        print('+' + x * '-' + '+')
        break

a = int(input('Podaj szerokość prostokata: '))
b = int(input('Podaj wysokość prostokata: '))
prostokat(a,b)

# 6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
# bn = input ('Podaj liczbę w formacie binarnym ')
# if bn.isnumeric():
#     def przeliczenie(bn):
#         wzor = (int(bn[0])*2**5)+(int(bn[1])*2**4)+(int(bn[2])*2**3)+(int(bn[3])*2**2)+(int(bn[4])*2**1)+(int(bn[5])*2**0)
#         return wzor
#     wynik = przeliczenie(bn)
#     print (f'Podana liczba w systemie dziesiętnym to {wynik}')
# else:
#     print('Podana wartość nie jest wartością liczbową')

# 7. Napisz program do rozpoznawania czy podana liczba jest parzysta czy nie.
# def parzysta(a):
#     if (int(a)%2==0):
#         return 'parzysta'
#     else:
#         return 'nieparzysta'
#
#
# number = input('Podaj liczbę ')
# if number.isnumeric():
#     print (f'Podana liczba jest {parzysta(number)}')
# else:
#     print('Podana wartość nie jest wartością liczbową')


# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
# def podzielnosc(a):
#     if (float(a)%3==0) or (float(a)%5==0) or (float(a)%7==0):
#         return 'jest podzielna przez 3 lub 5 lub 7'
#     else:
#         return 'nie dzieli się przez 3, 5, 7'
#
#
# number = input('Podaj liczbę ')
# if number.isnumeric():
#     print (f'Podana liczba {podzielnosc(number)}')
# else:
#     print('Podana wartość nie jest wartością liczbową')

# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
# def podzielnosc(a):
#     if (float(a)%3==0) and (float(a)%5==0) and (float(a)%7==0):
#         return 'jest podzielna przez 3 i 5 i 7'
#     else:
#         return 'nie dzieli się przez 3 i 5 i 7'
#
#
# number = input('Podaj liczbę ')
# if number.isnumeric():
#     print (f'Podana liczba {podzielnosc(number)}')
# else:
#     print('Podana wartość nie jest wartością liczbową')

# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
# def rok(a):
#     if (float(a)%4==0) and (float(a)%100!=0):
#         return 'Podany rok jest rokiem przestępnym'
#     elif (float(a%400==0)):
#         return 'Podany rok jest rokiem przestępnym'
#     else:
#         return 'Podany rok nie jest rokiem przestępnym'
#
#
# date = input('Podaj rok ')
# if date.isnumeric():
#     print (f'{rok(date)}')
# else:
#     print('Podana wartość nie jest wartością liczbową')


