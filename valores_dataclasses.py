from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str = 'Missing'
    sobrenome: str = 'Missing'
    # Se eu quiser que um valor MUTAVEL tenha padrão, devo usar isso.
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Allan', 'Giovanni')
    print(p1)
