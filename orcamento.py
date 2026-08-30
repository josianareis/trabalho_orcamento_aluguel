class Orcamento:
    VALOR_CONTRATO = 2000.00

    def __init__(self, nome_cliente, imovel, quantidade_parcelas):
        if not nome_cliente.strip():
            raise ValueError("O nome do cliente deve ser informado.")

        if quantidade_parcelas < 1 or quantidade_parcelas > 5:
            raise ValueError(
                "O contrato deve ser parcelado entre 1 e 5 vezes."
            )

        self.nome_cliente = nome_cliente
        self.imovel = imovel
        self.quantidade_parcelas = quantidade_parcelas

    def calcular_parcela_contrato(self):
        return self.VALOR_CONTRATO / self.quantidade_parcelas

    def gerar_planejamento_anual(self):
        aluguel = self.imovel.calcular_aluguel()
        parcela_contrato = self.calcular_parcela_contrato()
        planejamento = []

        for mes in range(1, 13):
            if mes <= self.quantidade_parcelas:
                contrato_no_mes = parcela_contrato
            else:
                contrato_no_mes = 0.00

            total_mes = aluguel + contrato_no_mes

            dados_mes = {
                "mes": mes,
                "aluguel": aluguel,
                "parcela_contrato": contrato_no_mes,
                "total_mes": total_mes
            }

            planejamento.append(dados_mes)

        return planejamento