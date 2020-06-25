import zajecia.moduly.walidator
import COVID19Py
import matplotlib.pyplot as mpl


# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym


def year():
    date = input('Enter the year ')
    if zajecia.moduly.walidator.validation(date) == True:
        if (float(date) % 4 == 0) and (float(date) % 100 != 0 or float(date) % 400 == 0):
            print('This is a leap year')
        else:
            print('This is not a leap year')

# 12. Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 wydając ich jak najmniej.


def change_money():
    coins = {5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    amount = float(input('Enter the amount to change '))
    if zajecia.moduly.walidator.validation(amount) == True:
        for i in coins:
            numAmount = (amount // i)
            amount -= numAmount * i
            coins[i] = int(numAmount)
        for i in coins:
            if coins[i] != 0:
                print(f'You need {coins[i]} x {i} zł')

# 14. Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata


def dog_age():
    x = int(input('How old is you dog in human years? '))
    if zajecia.moduly.walidator.validation(x) == True:
        if x <= 2:
            age = x * 10.5
            print(f'Your dog is {age} dog\'s old')
        else:
            age = 21 + (x - 2) * 4
            print(f'Your dog is {age} dog\'s old')

# 17. Zadanie z rysowaniem wykresu zachorowań na COVID-19.


def covid19():
    covid19 = COVID19Py.COVID19()
    data = covid19.getAll(timelines=True)
    virusdetails = dict(data['latest'])
    names = list(virusdetails.keys())
    values = list(virusdetails.values())
    mpl.bar(range(len(virusdetails)), values, tick_label=names)
    mpl.show()
    print(virusdetails)