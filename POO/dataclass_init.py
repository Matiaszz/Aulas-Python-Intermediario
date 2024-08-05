from dataclasses import dataclass


# Se a gente chamar esse decorator, a gente pode configurar ele do jeito que a gente quiser, nessa aula vi: init = False (desativa o init e voce tem que configurar dentro da classe) | frozen = True (Deixa a classe constante (intalteravel) | repr=False (desativa o repr e tenho que defini-lo na classe) | order=True (ordena )
@dataclass(frozen=True, order=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        # self.nome = 'João'  # (frozen=True | Dá Erro)
        pass

    def printar(self):
        nomecompleto = f'{self.nome} {self.sobrenome}'
        return nomecompleto


if __name__ == '__main__':
    p1 = [Pessoa('Allan', 'Giovanni'), Pessoa(
        'Davi', 'Balieiro'),  Pessoa('Matheus', 'José')]
    ordena = sorted(p1, reverse=True)  # Lista ordenada reversamente
    # ordena = sorted(p1, reverse=True, key=lambda p: p.sobrenome)
    print(ordena)
