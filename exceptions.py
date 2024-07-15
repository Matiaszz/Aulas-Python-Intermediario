class MyError(Exception):
    pass


class OtherError(Exception):
    pass


def raise_error():
    var_error = MyError('Mensagem de erro', 'Outra mensagem aleatoria')
    var_error.add_note('Uma nota para comunicar o que errou com outros devs')

    raise var_error


try:
    raise_error()  # vai dar erro e cair no except
except (MyError, OtherError) as error:
    print(error, '|', error.__class__.__name__)
    exception_ = OtherError('Outro errinho')
    exception_.add_note('Aconteceu outro erro')
    # Lança outro erro dizendo que por causa do raise_error() causou o erro exception_
    raise exception_
