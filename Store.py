class Store:

    def __init__(self):
        self.products = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
        self.prices = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
        self.stocks = {1: 50, 2: 45, 3: 30, 4: 15}
        self.index = 5

    def show(self):
        print("\n")
        print("========================================")
        print("Lista de Productos:")
        print("========================================")
        for (k1, v1), (k2, v2), (k3, v3) in zip(self.products.items(), self.prices.items(), self.stocks.items()):
            print("{0:<4} {1:<16} {2:>8} {3:>8}".format(k1, v1, v2, v3))
        print("========================================")

    def add(self, product, price, stock):
        self.products[self.index] = product
        self.prices[self.index] = price
        self.stocks[self.index] = stock
        self.index += 1

    def delete(self, id_):
        self.products.pop(id_)
        self.prices.pop(id_)
        self.stocks.pop(id_)

    def update(self, id_, product, price, stock):
        self.products[id_] = product
        self.prices[id_] = price
        self.stocks[id_] = stock

    def checkId(self, id_):
        return id_ in self.products and id_ in self.prices and id_ in self.stocks
