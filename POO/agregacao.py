class CarrinhoDeCompras:
    def __init__(self):
        self._products = []

    def total_price(self):
        return sum([p.preco
                    for p in self._products
                    ])

    def insire_products(self, *products):
        # for produto in products:
        #     self._products.append(produto)

        self._products += products  # faz a mesma coisa que o comentario de cima

    def list_products(self):
        print()
        for prod in self._products:
            print(prod.nome, prod.preco)
        print()
        return


class product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoDeCompras()
p1 = product('Piso', 55.90)
p2 = product('Caneta', 1.20)
carrinho.insire_products(p1, p2)

print(carrinho.list_products())
print(round(carrinho.total_price(), 2))
