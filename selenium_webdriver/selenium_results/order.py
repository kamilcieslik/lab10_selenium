from datetime import datetime


class Order(object):

    def __init__(self, seller: str,
                 purchase_date: object, price: float,
                 price_with_delivery: float, number_of_elements: int = 1):
        self._seller = seller
        self._purchase_date = datetime.strptime(purchase_date, '%d.%m.%Y, '
                                                               '%H:%M')
        self._price = price
        self._delivery = price_with_delivery - price
        self._number_of_elements = number_of_elements

    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, seller):
        self._seller = seller

    @property
    def purchase_date(self):
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        self._purchase_date = purchase_date

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def delivery(self):
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        self._delivery = delivery

    @property
    def number_of_elements(self):
        return self._price

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        self._number_of_elements = number_of_elements

    def __str__(self) -> str:
        return "(sprzedawca: "+self._seller + ", data zakupu: " \
               + str(self._purchase_date) + ", cena: " + str(self._price) \
               + ", cena dostawy: " + str(round(self._delivery, 2)) \
               + ", szt.: " + str(self._number_of_elements) + ")"

    def __repr__(self) -> str:
        return "(sprzedawca: "+self._seller + ", data zakupu: " \
               + str(self._purchase_date) + ", cena: " + str(self._price) \
               + ", cena dostawy: " + str(round(self._delivery, 2)) \
               + ", szt.: " + str(self._number_of_elements) + ")"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
