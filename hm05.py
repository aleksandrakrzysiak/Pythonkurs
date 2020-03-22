# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
def c_t_f():
    try:
        temperature = input('Podaj ilosc stopni Celsjusza ')
        wzor = 32 + 9/5 * float(temperature)
        print(f'Ilosc stopni Fahrenheita to {wzor}')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
def f_t_c():
    try:
        temperature = input('Podaj ilosc stopni Fahrenheita ')
        wzor = 5/9*(float(temperature)-32)
        print(f'Ilosc stopni Fahrenheita to {wzor}')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
def pole_kola():
    try:
        r = input('Podaj dlugosc promienia kola w centymetrach ')
        wzor = 3.14 * float(r)**2
        print(f'Pole kola o zadanym promieniu to {wzor}')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
def digit():
    try:
        number = input('Podaj liczbę ')
        liczba = float(number)
        print(f'Pierwsza cyfra to {number[0]}')
        print(f'Ostatnia cyfra to {number[-1]}')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +-------+
#     |       |
#     |       |
#     +-------+

def prostokat():
    try:
        x = int(input('Podaj szerokość prostokąta '))
        y = int(input('Podaj wysokość prostokąta '))
        print('+' + x * '-' + '+')
        print(y*('|'+(' '* x ) + '|'+ '\n'), end='')
        print('+' + x * '-' + '+')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
def przeliczenie():
    try:
        bn = input('Podaj liczbę w formacie binarnym ')
        wzor = (int(bn[0])*2**5)+(int(bn[1])*2**4)+(int(bn[2])*2**3)+(int(bn[3])*2**2)+(int(bn[4])*2**1)+(int(bn[5])*2**0)
        print(f'Podana liczba w systemie dziesiętnym to {wzor}')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 7. Napisz program do rozpoznawania czy podana liczba jest parzysta czy nie.
def parzysta():
    try:
        number = input('Podaj liczbę całkowitą ')
        if (int(number) % 2 == 0):
            print(f'Podana liczba jest parzysta')
        else:
            print(f'Podana liczba jest nieparzysta')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
def dziel_lub():
    try:
        a = input('Podaj liczbę ')
        if (float(a) % 3 == 0) or (float(a) % 5 == 0) or (float(a) % 7 == 0):
            print('Liczba jest podzielna przez 3 lub 5 lub 7')
        else:
            print('Liczba nie dzieli się przez 3, 5, 7')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
def dziel_i():
    try:
        a = input('Podaj liczbę ')
        if (float(a) % 3 == 0) and (float(a) % 5 == 0) and (float(a) % 7 == 0):
            print('Liczba jest podzielna przez 3 i 5 i 7')
        else:
            print('Liczba nie dzieli się przez 3 i 5 i 7')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
def rok():
    try:
        date = input('Podaj rok ')
        if (float(date) % 4 == 0) and (float(date) % 100 != 0 or float(date) % 400 ==0):
            print('Podany rok jest rokiem przestępnym')
        else:
            print('Podany rok nie jest rokiem przestępnym')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')
#
# 11. Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)
#
def rysowanie():
    lista =input ('Podaj dowolne elementy listy odzielone przecinkami: ')
    lista = lista.split(',')
    print(lista)
    for i in range(len(lista)):
        print('+' + 10 * '-' + '+')
        if len(lista[i]) < 10:
            print('|' + lista[i] + ' '*(10-len(lista[i])) + '|')
        else:
            print('|' + lista[i][:7]+'...' + ' ' * (7 - len(lista[i])) + '|')
        print('+' + 10 * '-' + '+')

# 12. Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 wydając ich jak najmniej.
def rozmieniam():
    monety = {5:0, 2:0, 1:0, 0.5:0, 0.2:0, 0.1:0, 0.05:0, 0.02:0, 0.01:0}
    try:
        kwota = float(input('Kwota, którą chcesz rozmienić: '))
        for i in monety:
            numAmount = (kwota//i)
            kwota -= numAmount*i
            monety[i] = int(numAmount)
        for i in monety:
            if monety[i] !=0:
                print(f'Potrzebujesz {monety[i]} razy {i} zł')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 13. Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####

def piramida():
    try:
        n = int(input('Podaj wysokość piramidy: '))
        for i in range(n):
            print(' ' *(n-i-1)+'#'*(2*i+1))
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 14. Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata
def wiek_psa():
    try:
        x = int(input('Ile ludzkich lat ma Twój pies? '))
        if x<=2:
            wiek=x*10.5
            print(f'Wiek Twojego psa to {wiek} lata psie')
        else:
            wiek=21+(x-2)*4
            print(f'Wiek Twojego psa to {wiek} lata psie')
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')

# 15. Nakładka na program
def menu():
    print("Witaj w Multitoolu :)")
    print()
    print('Wybierz program, który chcesz wykonać:')
    choice = True
    while choice:
        print('''
        1. Przeliczanie stopni Celsjusza na Fahrenheita
        2. Przeliczanie stopni Fahrenheita na Celsjusza
        3. Obliczanie pola powierzchni koła
        4. Pierwsza i ostatnia cyfra podanej liczby
        5. Rysowanie prostokąta o zadanych parametrach
        6. Zamiana liczby birnarnej na dziesiętną
        7. Sprawdzanie czy zadana liczba jest parzysta
        8. Sprawdzanie czy zadana liczba jest podzielna przez 3 lub 5 lub 7
        9. Sprawdzanie czy zadana liczba jest podzielna przez 3 i 5 i 7
        10. Sprawdzanie czy rok jest przestępny
        11. Rysowanie dowolnej listy
        12. Rozmienianie pieniędzy
        13. Rysowanie piramidy o zdanej wysokości
        14. Obliczanie wieku psa
        15. Program losowy
        16. Wyjście z programu
        ''')
        choice=input('Twój wybór: ')
        if choice == "1":
            c_t_f()
        elif choice == "2":
            f_t_c()
        elif choice == "3":
            pole_kola()
        elif choice == "4":
            digit()
        elif choice == "5":
            prostokat()
        elif choice == "6":
            przeliczenie()
        elif choice == "7":
            parzysta()
        elif choice == "8":
            dziel_lub()
        elif choice == "9":
            dziel_i()
        elif choice == "10":
            rok()
        elif choice == "11":
            rysowanie()
        elif choice == "12":
            rozmieniam()
        elif choice == "13":
            piramida()
        elif choice == "14":
            wiek_psa()
        elif choice == "15":
           pass #losowanie zadania
        elif choice =="16":
            print('Do zobaczenia!')
            break
        else:
            print('Nie ma takiego programu, sprobuj jeszcze raz.')
        print()
        czy_kontynuowac = input('Czy kontynuować program [T/N]? ')
        if czy_kontynuowac == 'T' or czy_kontynuowac == 't':
            choice = True
        else:
            print('Dziękuję, do zobaczenia!')
            break
menu()
