def walidacja(x):
    try:
        float(x)
        return True
    except:
        print('To nie jest liczba. Podaj jeszcze raz.')
        return False