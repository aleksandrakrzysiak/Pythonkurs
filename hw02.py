# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
temperature = input ('Podaj ilosc stopni Celsjusza ')
c_t_f = 32 + 9/5 * float(temperature)
print ('Ilosc stopni Fahrenheita to:', c_t_f)

# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
temperature = input ('Podaj ilosc stopni Fahrenheita ')
f_t_c = 5/9*(float(temperature)-32)
print ('Ilosc stopni Celsjusza to:', f_t_c)

# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
promien = input ('Podaj dlugosc promienia kola w centymetrach ')
pole = 3.14 * float(promien)**2
print ('Pole kola wynosi', pole)

# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
number = input('Podaj liczbę ')
print ('Pierwsza cyfra to', number[0])
print ('Ostatnia cyfra to', number[-1])

# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +-------+
#     |       |
#     |       |
#     +-------+

wysokosc = int(input ('Podaj wysokość prostokąta '))
szerokosc = int(input ('Podaj szerokość prostokąta '))
print ('+' + wysokosc * '-' + '+' )
print (szerokosc * ('|' + (wysokosc *' ')+ '|'+'\n'))
# za dużo o jedną pustą linię :(
print ('+' + wysokosc * '-' + '+')

# 6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
bn = input ('Podaj liczbę w formacie binarnym ')
przeliczenie = (int(bn[0])*2**5)+(int(bn[1])*2**4)+(int(bn[2])*2**3)+(int(bn[3])*2**2)+(int(bn[4])*2**1)+(int(bn[5])*2**0)
print ('Podana liczba w systemie dziesiętnym to', przeliczenie)

# 7. Napisz program do rozpoznawania czy podana liczba jest parzysta czy nie.
number = float(input ('Podaj liczbę '))
if (number%2==0):
    print ('Podana liczba jest parzysta')
else:
    print ('Podana liczba nie jest parzysta')

# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
number = float(input ('Podaj liczbę '))
if (number%3==0):
    print ('Podana liczba jest podzielna przez 3')
elif (number%5==0):
    print ('Podana liczba jest podzielna przez 5')
elif (number%7==0):
    print ('Podana liczba jest podzielna przez 7')
else:
    print ('Podana liczba nie dzieli się przez 3,5,7')

# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
number = float(input ('Podaj liczbę '))
if (number%3==0 and number%5==0 and number%7==0):
    print ('Podana liczba dzieli się przez 3 i 5 i 7')
else:
    print ('Podana liczba nie dzieli się przez 3 i 5 i 7')

# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
date = float(input('Podaj rok '))
if (date%4==0 and date%100!=0):
    print ('Podany rok jest rokiem przestępnym')
elif (date%400==0):
    print ('Podany rok jest rokiem przestępnym')
else:
    print ('Podany rok nie jest rokiem przestępnym')


