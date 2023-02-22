from Option import Option
import IO


class OptionDelete(Option):

    def __init__(self, title, store):
        super().__init__(title)
        self.store = store

    def execute(self):
        id_ = IO.get_int("ID del producto a eliminar: ")
        if self.store.checkId(id_):
            self.store.delete(id_)
        else:
            print("El ID del producto no existe!")