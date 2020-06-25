import zajecia.moduly.walidator

# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)


def c_t_f():
    temperature = input('Give the number of Celsius degrees ')
    if zajecia.moduly.walidator.validation(temperature) == True:
        equation = 32 + 9/5 * float(temperature)
        print(f'Number of Celsius degrees: {equation}')

# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)


def f_t_c():
    temperature = input('Give the number of Fahrenheit degrees ')
    if zajecia.moduly.walidator.validation(temperature) == True:
        equation = 5/9*(float(temperature)-32)
        print(f'Number of Fahrenheit degrees: {equation}')

