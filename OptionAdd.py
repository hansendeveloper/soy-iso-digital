from Option import Option
import IO


class OptionAdd(Option):

    def __init__(self, title, store):
        super().__init__(title)
        self.store = store

    def execute(self):
        product = IO.get_str("Introduzca producto: ")
        price = IO.get_float("Introduzca precio: ")
        stock = IO.get_int("Introduzca stock: ")
        self.store.add(product, price, stock)
