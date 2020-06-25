import datetime


class Item(object):
    vat = 7

    def __init__(self, id, title, quantity= 100, price= 19.99):
        self.id = id
        self.title = title
        self.created_at = datetime.datetime.now()
        self.last_buy_at = datetime.datetime.now()
        self.quantity = quantity
        self.price = price

    @classmethod
    def inny_vat(cls, vat_new):
        if vat_new > 5 and vat_new < 22:
            cls.vat = vat_new
        else:
            return f'Wrong value, VAT is {cls.vat}%'

    def gross_price(self):
        return round(self.price * (100 + self.vat) / 100, 2)
