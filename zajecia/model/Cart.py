from zajecia.model.Book import Book
from zajecia.model.Ebook import Ebook


class Cart():
    def __init__(self):
        self.elementy = []
        self.ilosc_elementow = 0
        self.net = 0
        self.gross = 0

    def dodaj(self, element):
        self.elementy.append(element)
        self.ilosc_elementow += 1
        self.net = self.net + element.price
        self.gross = self.gross + element.gross_price()

    def __len__(self):
        return len(self.elementy)

    def net_value(self):
        return self.net

    def gross_value(self):
        return self.gross

    # pokaz koszyk:
    def __str__(self):
        return f"Your cart: {self.elementy}, quantity: {self.__len__()}, amount: {self.gross}"

koszyk = Cart()
ksiazka_1 = Book(1, 'Potop', 'Sienkiewicz', 300)
ksiazka_2 = Book(2, 'Trylogia', 'Sienkiewicz', 1300)
ebook_1 = Ebook(3, 'Potop', 'Sienkiewicz', 30)

koszyk.dodaj(ksiazka_1)
koszyk.dodaj(ksiazka_2)
koszyk.dodaj(ebook_1)

print(f"Ilość w koszyku: {len(koszyk)}")
print(f"Wartość netto: {koszyk.net_value()}")
print(f"Wartość brutto: {koszyk.gross_value()}")