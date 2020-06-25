import zajecia.moduly.temperatury
import zajecia.moduly.matematyczne
import zajecia.moduly.rysowanie
import zajecia.moduly.zyciowe
import zajecia.moduly.walidator
from random import randint
import csv


def random_task():
    random = randint(1, 16)
    print(f'You got {random}')
    tasks[f'{random}']['call']()


def exit_program():
    print('Goodbye!')
    exit()


def menu(tasks):
    print('Welcome to the Multitool :)')
    for index, task in tasks.items():
        print(f'Exercise {index} - {task["name"]}')
    return input('Select the program you would like to run, please ').upper()


tasks = {"1": {'name': 'Converting Celsius to Fahrenheit', 'call': zajecia.moduly.temperatury.c_t_f},
         "2": {'name': 'Converting Fahrenheit to Celsius', 'call': zajecia.moduly.temperatury.f_t_c},
         "3": {'name': 'Counting the surface of the circle', 'call': zajecia.moduly.matematyczne.circular_field},
         "4": {'name': 'First and last digit of the given number', 'call': zajecia.moduly.matematyczne.digit},
         "5": {'name': 'Drawing rectangle', 'call': zajecia.moduly.rysowanie.rectangle},
         "6": {'name': 'Converting binar number to decimal number', 'call': zajecia.moduly.matematyczne.conversion},
         "7": {'name': 'Is it even number?', 'call': zajecia.moduly.matematyczne.even},
         "8": {'name': 'Divisibility of numbers by 3 or 5 or 7', 'call': zajecia.moduly.matematyczne.divide_or},
         "9": {'name': 'Divisibility of numbers by 3 and 5 and 7', 'call': zajecia.moduly.matematyczne.divide_and},
         "10": {'name': 'Is it a leap year?', 'call': zajecia.moduly.zyciowe.year},
         "11": {'name': 'List drawing', 'call': zajecia.moduly.rysowanie.list_drawing},
         "12": {'name': 'Changing the money', 'call': zajecia.moduly.zyciowe.change_money},
         "13": {'name': 'Pyramid drawing', 'call': zajecia.moduly.rysowanie.pyramid},
         "14": {'name': 'How old is your dog?', 'call': zajecia.moduly.zyciowe.dog_age},
         "15": {'name': 'Text statistics', 'call': zajecia.moduly.matematyczne.text_stats()},
         "16": {'name': 'COVID-19 graph', 'call': zajecia.moduly.zyciowe.covid19},
         "17": {'name': 'Random program', 'call': random_task},
         "18": {'name': 'Exit', 'call': exit_program},
         # "S": {'nazwa':'Statystki', 'call': statystki},
         }


def call_counter(menu):
    def helper(tasks):
        helper.calls += 1
        return menu(tasks)

    helper.calls = 0
    return helper


choice = None
with open('stats.csv', 'w+', encoding='utf-8') as file:
    fieldnames = ['Exercise', 'times']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    counter_m = 0
    while choice != '18':
        choice = menu(tasks)
        counter_m += 1
        try:
            tasks[choice]['call']()
            continuing = input('Do you want to contiune [Y/N]? ')
            if continuing == 'Y' or continuing == 'y':
                choice = True
            else:
                print('Thank you, goodbye!')
                break
        except KeyError:
            print('There is no such program. Please try again.')
    for choice in tasks.keys():
        x = choice
        # have to add here number of function calls
        writer.writerows([{'Exercise': f'{choice}', 'times': f'{x}'}])
    writer.writerows([{'Exercise': 'Menu', 'times': f'{counter_m}'}])

# choice = None
# while choice !='19':
#     choice = menu(zadania)
#     def licz():
#         ilosc = zadania[choice]['call']()
#         try:
#             ilosc = int(ilosc)
#             ilosc +=1
#         except:
#             ilosc = 1
#         print(f'funkcja {choice} zostala wybrana {ilosc}')

# def statystyki():
#     with open('stats.csv', 'w', encoding='utf-8') as file:
#         writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         licznik_m = 0
#         if menu(zadania) == True:
#             licznik_m +=1
#             writer.writerow([f'Menu: {licznik_m}'])
# if choice in zadania.items():
#
#
# choice = menu(zadania)
# try:
#     choice = int(choice)
#     choice += 1
# except:
#     choice = 1
# writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# writer.writerow([f'Menu: {choice}'])

# def statscsv1():
#     ilosc_uruchomien_menu = Counter(menu(zadania))
#     with open('stats.csv', 'w', encoding='utf-8') as file:
#         fieldnames = ['Zadanie', 'Ilość uruchomień']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow(f'{zadania.items()}': f'{ilosc_uruchomien_menu}'})
# for index in zadania.items():
#     writer.writerow(f'Zadanie {index} zostało uruchomione {ilosc_uruchomien_menu} razy')
