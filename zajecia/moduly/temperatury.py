import zajecia.moduly.walidator

# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
def c_t_f():
    temperature = input('Podaj ilosc stopni Celsjusza ')
    if zajecia.moduly.walidator.walidacja(temperature) == True:
        wzor = 32 + 9/5 * float(temperature)
        print(f'Ilosc stopni Fahrenheita to {wzor}')

# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
def f_t_c():
    temperature = input('Podaj ilosc stopni Fahrenheita ')
    if zajecia.moduly.walidator.walidacja(temperature) == True:
        wzor = 5/9*(float(temperature)-32)
        print(f'Ilosc stopni Fahrenheita to {wzor}')

