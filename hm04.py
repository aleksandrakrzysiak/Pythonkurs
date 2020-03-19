# 2) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)


# 3) Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 wydając ich jak najmniej.


# kwota = float(input('Podaj kwotę '))
# monety = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
# monety_back = []
# for i in monety:
#     while kwota>=i:
#         monety_back.append(i)
#         kwota = kwota-i
#
# print(monety_back)
# print(f'{monety_back.count(5)}')
#
#
# for i in [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
#     while (kwota>=i):
#         i +=1
#         kwota = kwota-i
#     print (il_5, il_2, il_1)
# kwota = float(input('Kwota: '))
# a = 5
# b = 2
# c = 1
# d = 0.5
# e = 0.25
# f = 0.1
# g = 0.05
# h = 0.02
# j = 0.01
# monety = {a:0,b:0,c:0,d:0,e:0,f:0,g:0,h:0,j:0}
# for i in monety:
#     numAmount = (kwota//i)
#     kwota -= numAmount*i
#     monety[i] = int(numAmount)
#
#
# print(monety)

# kwota = float(input('Kwota: '))
#
# monety = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
# for i in monety:
#     numAmount = (kwota)//i
#     kwota -= numAmount*i
#     monety.append(numAmount)
#
#
# print(zip(monety, numAmount))


# 4) Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####

# def piramida(n):
#     for i in range(n):
#         print(' ' *(n-i-1)+'#'*(2*i+1))
#
#
# wysokosc = int(input('Podaj wysokość piramidy: '))
# piramida(wysokosc)

# 5) Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata
# def wiek(x):
#     if x<=2:
#         n=x*10.5
#         return n
#     else:
#         n=21+(x-2)*4
#         return n
#
#
# dog = int(input('Ile ludzkich lat ma Twój pies? '))
# print(f'Wiek Twojego psa to {wiek(dog)} lata psie')

