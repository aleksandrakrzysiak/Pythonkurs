import moduly.walidator
# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
def rok():
    date = input('Podaj rok ')
    if moduly.walidator.walidacja(date) == True:
        if (float(date) % 4 == 0) and (float(date) % 100 != 0 or float(date) % 400 == 0):
            print('Podany rok jest rokiem przestępnym')
        else:
            print('Podany rok nie jest rokiem przestępnym')

# 12. Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 wydając ich jak najmniej.
def rozmieniam():
    monety = {5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    kwota = float(input('Kwota, którą chcesz rozmienić: '))
    if moduly.walidator.walidacja(kwota) == True:
        for i in monety:
            numAmount = (kwota // i)
            kwota -= numAmount * i
            monety[i] = int(numAmount)
        for i in monety:
            if monety[i] != 0:
                print(f'Potrzebujesz {monety[i]} razy {i} zł')

# 14. Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata
def wiek_psa():
    x = int(input('Ile ludzkich lat ma Twój pies? '))
    if moduly.walidator.walidacja(x) == True:
        if x <= 2:
            wiek = x * 10.5
            print(f'Wiek Twojego psa to {wiek} lata psie')
        else:
            wiek = 21 + (x - 2) * 4
            print(f'Wiek Twojego psa to {wiek} lata psie')