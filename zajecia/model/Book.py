from zajecia.model.Item import Item


class Book(Item):
    def __init__(self, id, title, author, number_of_pages):
        super().__init__(id, title)
        self.author = author
        self.number_of_pages = number_of_pages

    # wyswietlenie ksiazki:
    def __str__(self):
        return f"Autor: {self.author.capitalize()}, tytuł: {self.title.capitalize()}"

    def __len__(self):
        return self.number_of_pages

    def __add__(self, other):
        #spr czy inna ksiazka istnieje, aby add zadzialal
        # moze zrobic do itema i sprawdzac quantity?
        if isinstance(other, Book):
            return self.number_of_pages + other.number_of_pages
        else:
            print('No book added')
            return self.number_of_pages