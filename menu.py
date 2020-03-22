import moduly.temperatury
import moduly.matematyczne
import moduly.rysowanie
import moduly.zyciowe
import moduly.walidator
from random import randint

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
        choice = input('Twój wybór: ')
        if choice == "1":
            moduly.temperatury.c_t_f()
        elif choice == "2":
            moduly.temperatury.f_t_c()
        elif choice == "3":
            moduly.matematyczne.pole_kola()
        elif choice == "4":
            moduly.matematyczne.digit()
        elif choice == "5":
            moduly.rysowanie.prostokat()
        elif choice == "6":
            moduly.matematyczne.przeliczenie()
        elif choice == "7":
            moduly.matematyczne.parzysta()
        elif choice == "8":
            moduly.matematyczne.dziel_lub()
        elif choice == "9":
            moduly.matematyczne.dziel_i()
        elif choice == "10":
            moduly.zyciowe.rok()
        elif choice == "11":
            moduly.rysowanie.rysowanie()
        elif choice == "12":
            moduly.zyciowe.rozmieniam()
        elif choice == "13":
            moduly.rysowanie.piramida()
        elif choice == "14":
            moduly.zyciowe.wiek_psa()
        elif choice == "15":
            print(f'Wylosowano zadanie {randint(1,14)}')
            continue
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