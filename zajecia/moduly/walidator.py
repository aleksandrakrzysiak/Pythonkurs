def validation(x):
    try:
        float(x)
        return True
    except:
        print('This is not a number. Please try again.')
        return False

