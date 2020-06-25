from zajecia.model.Book import Book


class Ebook(Book):
    vat = 23
    format = 'pdf'

    def __init__(self, id, title, author, number_of_pages):
        super().__init__(id, title, author, number_of_pages)