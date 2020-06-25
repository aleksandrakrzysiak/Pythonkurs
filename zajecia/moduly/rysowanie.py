import zajecia.moduly.walidator


# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +-------+
#     |       |
#     |       |
#     +-------+


def rectangle():
    x = int(input('Enter the width of the rectangle '))
    y = int(input('Enter the height of the rectangle '))
    if zajecia.moduly.walidator.validation(x) == True:
        if zajecia.moduly.walidator.validation(y) == True:
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


def list_drawing():
    try:
        print("All symbols that you will give between list's elements will be the part of this list")
        data = input ('Please enter elements with one space between ')
        your_list = data.split()
        print(your_list)
        print(f'Your list: {your_list}')
        y = len(your_list)  # liczba elementow w liscie
        up = y * ('+' + 10 * '-') + '+' + '\n'
        down = '\n' + y * ('+' + 10 * '-') + '+'

        new_list = []
        for i, item in enumerate(your_list):
            x = len(item)
            if len(item) >10:
                item = item[:7] +'...'
            else:
                item = item + (10 - x) * ' '
            new_list.insert(i, item)
        print(up + '|' + '|'.join(new_list) + '|' + down)
    except:
        print('Incorrect formatted data. Please try again.')

# 13. Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####


def pyramid():
    n = int(input('Enter the height of the pyramid '))
    if zajecia.moduly.walidator.validation(n) == True:
        for i in range(n):
            print(' ' *(n-i-1)+'#'*(2*i+1))
