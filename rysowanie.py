import moduly.walidator
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
    x = int(input('Podaj szerokość prostokąta '))
    y = int(input('Podaj wysokość prostokąta '))
    if moduly.walidator.walidacja(x) == True:
        if moduly.walidator.walidacja(y) == True:
            print('+' + x * '-' + '+')
            print(y*('|'+(' '* x ) + '|'+ '\n'), end='')
            print('+' + x * '-' + '+')
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
# 13. Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####

def piramida():
    n = int(input('Podaj wysokość piramidy: '))
    if moduly.walidator.walidacja(n) == True:
        for i in range(n):
            print(' ' *(n-i-1)+'#'*(2*i+1))
