from Store import Store
from Menu import Menu


class Warehouse:

    def __init__(self):
        self.store = Store()
        self.menu = Menu(self.store)

    def execute(self):
        while True:
            self.store.show()
            self.menu.show()
            self.menu.getOption().execute()
            if self.menu.isEnded():
                break
