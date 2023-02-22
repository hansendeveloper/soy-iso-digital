import IO
from OptionAdd import OptionAdd
from OptionDelete import OptionDelete
from OptionUpdate import OptionUpdate
from OptionExit import OptionExit


class Menu:

    def __init__(self, store):
        self.options = []
        self.options.append(OptionAdd("[1] Agregar", store))
        self.options.append(OptionDelete("[2] Eliminar", store))
        self.options.append(OptionUpdate("[3] Actualizar", store))
        self.exit = OptionExit("[4] Salir", store)
        self.options.append(self.exit)

    def show(self):
        print(*self.options, sep=", ")

    def getOption(self):
        while True:
            option = IO.get_int("\nElija opción [1-4]: ")
            error = [1, 2, 3, 4].count(option)
            if error > 0:
                break
            else:
                print("Error! La opción debe ser entre 1 y 4")
        return self.options[option - 1]

    def isEnded(self):
        return self.exit.isExecuted()
