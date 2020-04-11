import zajecia.moduly.temperatury
import zajecia.moduly.matematyczne
import zajecia.moduly.rysowanie
import zajecia.moduly.zyciowe
import zajecia.moduly.walidator
from random import randint

def zadanie_losowe():
    losowe = randint(1, 14)
    print(f'Wylosowano zadanie {losowe}')
    zadania[f'{losowe}']['call']()

def wyjscie():
    print('Dziękuję, do zobaczenia!')
    exit()

def menu(zadania):
    print('Witaj w Multitoolu :)')
    for index, zadanie in zadania.items():
        print(f'Zadanie {index} - {zadanie["nazwa"]}')

zadania = { "1": {'nazwa':'Przeliczanie stopni Celsjusza na Fahrenheita', 'call': zajecia.moduly.temperatury.c_t_f},
            "2": {'nazwa':'Przeliczanie stopni Fahrenheita na Celsjusza', 'call': zajecia.moduly.temperatury.f_t_c},
            "3": {'nazwa':'Obliczanie pola powierzchni koła', 'call': zajecia.moduly.matematyczne.pole_kola},
            "4": {'nazwa':'Pierwsza i ostatnia cyfra podanej liczby', 'call': zajecia.moduly.matematyczne.digit},
            "5": {'nazwa':'Rysowanie prostokąta o zadanych parametrach', 'call': zajecia.moduly.rysowanie.prostokat},
            "6": {'nazwa':'Zamiana liczby birnarnej na dziesiętną', 'call': zajecia.moduly.matematyczne.przeliczenie},
            "7": {'nazwa':'Sprawdzanie czy zadana liczba jest parzysta', 'call': zajecia.moduly.matematyczne.parzysta},
            "8": {'nazwa':'Podzielność liczby przez 3 lub 5 lub 7', 'call': zajecia.moduly.matematyczne.dziel_lub},
            "9": {'nazwa':'Podzielność liczby przez 3 i 5 i 7', 'call': zajecia.moduly.matematyczne.dziel_i},
            "10": {'nazwa':'Sprawdzanie czy rok jest przestępny', 'call': zajecia.moduly.zyciowe.rok},
            "11": {'nazwa':'Rysowanie dowolnej listy', 'call': zajecia.moduly.rysowanie.rysowanie},
            "12": {'nazwa':'Rozmienianie pieniędzy', 'call': zajecia.moduly.zyciowe.rozmieniam},
            "13": {'nazwa':'Rysowanie piramidy o zdanej wysokości', 'call': zajecia.moduly.rysowanie.piramida},
            "14": {'nazwa':'Obliczanie wieku psa', 'call': zajecia.moduly.zyciowe.wiek_psa},
            "15": {'nazwa':'Program losowy', 'call': zadanie_losowe},
            "16": {'nazwa':'Wyjście', 'call': wyjscie}
            }

menu(zadania)

choice = True
while choice:
    choice = input('Wybierz program, który chcesz wykonać: ')
    try:
        zadania[choice]['call']()
    except:
        print('Nie ma takiego programu. Spróbuj jeszcze raz.')
    czy_kontynuowac = input('Czy kontynuować program [T/N]? ')
    if czy_kontynuowac == 'T' or czy_kontynuowac == 't':
        choice = True
    else:
        print('Dziękuję, do zobaczenia!')
        break

