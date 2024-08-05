
from time import sleep
from threading import Thread
from threading import Lock


# class MyThread(Thread):
#     def __init__(self, text, time):
#         self.text = text
#         self.time = time
#         super().__init__()

#     def run(self):
#         sleep(self.time)
#         print(self.text)


# t1 = MyThread('Hello, World!', 5)
# t1.start()

# t2 = MyThread('trhead 2', 6)
# t2.start()

# t3 = MyThread('thread 3', 7)
# t3.start()


# for i in range(15):
#     print(i)
#     sleep(1)

########################################

# def vai_demorar(text, time):
#     sleep(time)
#     print(text)


# t = Thread(target=vai_demorar, args=('Olá Mundo', 2))
# t.start()

# while t.is_alive():
#     print('esperando')
#     sleep(1)

class Ingressos:
    def __init__(self, estoque: int) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, qtd: int):
        self.lock.acquire()

        if self.estoque < qtd:

            print(f'Não foi possivel realizar a compra por\
falta de itens, estoque:  {self.estoque}')
            self.lock.release()

            return
        sleep(1)

        self.estoque -= qtd
        print(f'Compra realizada com sucesso de {qtd} ingressos, resta:\
 {self.estoque}')
        self.lock.release()
        return


if __name__ == '__main__':
    cinema = Ingressos(10)

    for i in range(1, 15):
        t = Thread(target=cinema.comprar, args=(i,))
        t.start()

# self.lock.release = libera a "pessoa" da função
# self.lock.acquire = tranca a "porta" da função para os threads
# não entrar junto um do outro e causar uma confusão no codigo
