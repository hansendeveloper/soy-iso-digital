def get_int(prompt):
    while True:
        num = input(prompt)
        try:
            num = int(num)
            return num
        except ValueError:
            print("Debe introducir un número entero!")


def get_float(prompt):
    while True:
        num = input(prompt)
        try:
            num = float(num)
            return num
        except ValueError:
            print("Debe introducir un número!")


def get_str(prompt):
    while True:
        text = input(prompt)
        if text:
            return text
        else:
            print("Debe introducir una cadena de caracteres!")