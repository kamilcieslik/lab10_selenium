from selenium_webdriver.selenium_results.order import Order


class ResearcherResult(object):
    def __init__(self):
        self._oldest_order = Order
        self._orders = []

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, new_order):
        self._orders.append(new_order)

    @property
    def oldest_order(self):
        return self._oldest_order

    @oldest_order.setter
    def oldest_order(self, oldest_order):
        self._oldest_order = oldest_order

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
