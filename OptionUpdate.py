from Option import Option
import IO


class OptionUpdate(Option):

    def __init__(self, title, store):
        super().__init__(title)
        self.store = store

    def execute(self):
        id_ = IO.get_int("ID del producto a editar: ")
        if self.store.checkId(id_):
            product = IO.get_str("Introduzca producto: ")
            price = IO.get_float("Introduzca precio: ")
            stock = IO.get_int("Introduzca stock: ")
            self.store.update(id_, product, price, stock)
        else:
            print("El ID del producto no existe!")
