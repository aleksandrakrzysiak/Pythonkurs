def walidacja(x):
    try:
        float(x)
        return True
    except:
        print('To nie jest liczba. Spróbuj drugi raz.')
        return False
