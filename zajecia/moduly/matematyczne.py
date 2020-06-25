import zajecia.moduly.walidator
import re
import csv

# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)


def circular_field():
    r = input('Enter the circle radius in centimeters ')
    if zajecia.moduly.walidator.validation(r) == True:
        equation = 3.14 * float(r)**2
        print(f'Area equals {equation}')

# 7. Napisz program do rozpoznawania czy podana liczba jest parzysta czy nie.


def even():
    number = input('Enter an intiger value ')
    if zajecia.moduly.walidator.validation(number) == True:
        if int(number) % 2 == 0:
            print(f'Number is even')
        else:
            print(f'Number is odd')

# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7


def divide_or():
    a = input('Enter a number ')
    if zajecia.moduly.walidator.validation(a) == True:
        if (float(a) % 3 == 0) or (float(a) % 5 == 0) or (float(a) % 7 == 0):
            print('This number is divided by 3 or 5 or 7')
        else:
            print('This number is not divided by 3, 5, 7')

# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7


def divide_and():
    a = input('Enter a number ')
    if zajecia.moduly.walidator.validation(a) == True:
        if (float(a) % 3 == 0) and (float(a) % 5 == 0) and (float(a) % 7 == 0):
            print('This number is divided by 3 and 5 and 7')
        else:
            print('This number is not divided by 3 and 5 and 7')

# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby


def digit():
    number = input('Enter a number ')
    if zajecia.moduly.walidator.validation(number) == True:
        print(f'First digit: {number[0]}')
        print(f'Last digit: {number[-1]}')

# 6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.


def conversion():
    bn = input('Enter a number in binar format ')
    if zajecia.moduly.walidator.validation(bn) == True:
        equation = (int(bn[0])*2**5)+(int(bn[1])*2**4)+(int(bn[2])*2**3)+(int(bn[3])*2**2)+(int(bn[4])*2**1)+(int(bn[5])*2**0)
        print(f'Number in decimal format: {equation}')

# 15. Napisz program, który poda statystyki dowolnego tekstu z pobranego pliku, wypisze takie dane jak, np:
# ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
# Niech będzie możliwość wyboru trybu case sensitivity
# Niech program tworzy też plik ze statystyką swojej pracy


def text_stats():
    try:
        with open('satstxt.csv', 'r+', encoding='utf-8') as csvfile:
            with open(r'C:\Users\Ola\PycharmProjects\PythonkursGit\zajecia\moduly\python.txt', 'r') as file:
                text = file.read()
                line = len(re.findall(r'\n', text))
                words = len(re.findall(r'\w+', text))
                characters = len(re.findall(r'\S', text))
                uppercase = len(re.findall('[A-Z]', text))
                countA = text.count('a') + text.count('A')
                number = len(text)
                average = words // (line+1)
                print(f'Number of characters in the file: {number}')
                print(f'Average number of words in the file: {average}')
                print(f'Number of words in the file: {words}')
                print(f'Number of capital letters in the file: {uppercase}')
                print(f'Number of letters in the file: {characters}')
                print(f'Number of "A" letter in the file: {countA}')
                quantity = file.read()
                try:
                    quantity = int(quantity)
                    quantity +=1
                except:
                    quantity = 1
                csvfile.seek(0)
                writer = csv.writer(csvfile, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([f'Number of program launches: {quantity}'])

        # with open('satstxt.csv', 'r+', encoding='utf-8') as csvfile:
        #     try:
        #         text = int(text)
        #         text += 1
        #     except:
        #         text = 1
        #     writer = csv.writer(csvfile, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #     writer.writerow([f'Ilość uruchomień programu: {text}'])
        #     writer.writerow([f'Ilość znaków w całym pliku: {number}'])
        #     writer.writerow([f'Średnia ilość słów w całym pliku: {average}'])
        #     writer.writerow([f'Ilość słów w całym pliku: {words}'])
        #     writer.writerow([f'Ilość dużych liter w całym pliku: {uppercase}'])
        #     writer.writerow([f'Ilość liter w całym pliku: {characters}'])
        #     writer.writerow([f'Ilość literek \'A\' w całym pliku: {countA}'])
    except FileNotFoundError:
        print('There is no file to read')







