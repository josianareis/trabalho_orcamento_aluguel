
class Imovel:
    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base

    def calcular_aluguel(self):
        return self.valor_base

class Apartamento(Imovel):
    def __init__(self, quartos, tem_garagem, possui_criancas):
        super().__init__("Apartamento", 700.00)

        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.possui_criancas = possui_criancas

    def calcular_aluguel(self):
        valor = self.valor_base

        if self.quartos == 2:
            valor += 200.00

        if self.tem_garagem:
            valor += 300.00

        if not self.possui_criancas:
            valor *= 0.95

        return valor


class Casa (Imovel):
    def __init__(self, quartos, tem_garagem):
        super().__init__("Casa", 900.00)

        self.quartos = quartos
        self.tem_garagem = tem_garagem

    def calcular_aluguel(self):
        valor = self.valor_base

        if self.quartos == 2:
            valor += 250.00

        if self.tem_garagem:
            valor += 300.00

        return valor

class Estudio(Imovel):
    def __init__(self, quantidade_vagas):
        super().__init__("Estúdio", 1200.00)

        if quantidade_vagas < 0 or quantidade_vagas ==1:
            raise ValueError("O estúdio deve ter zero vaga ou, no mínimo, duas vagas.") 

        self.quantidade_vagas = quantidade_vagas

    def calcular_aluguel(self):
        valor = self.valor_base

        if self.quantidade_vagas >= 2:
            valor += 250.00

        if self.quantidade_vagas > 2:
            vagas_adicionais = self.quantidade_vagas - 2
            valor += vagas_adicionais * 60.00

        return valor