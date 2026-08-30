import csv


def formatar_valor_csv(valor):
    return f"{valor:.2f}".replace(".", ",")


def gerar_csv(orcamento, nome_arquivo):
    planejamento = orcamento.gerar_planejamento_anual()

    with open(
        nome_arquivo,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        escritor = csv.writer(
            arquivo,
            delimiter=";"
        )

        escritor.writerow([
            "Cliente",
            "Tipo de imóvel",
            "Mês",
            "Aluguel",
            "Parcela do contrato",
            "Total do mês"
        ])

        for dados_mes in planejamento:
            escritor.writerow([
                orcamento.nome_cliente,
                orcamento.imovel.tipo,
                dados_mes["mes"],
                formatar_valor_csv(dados_mes["aluguel"]),
                formatar_valor_csv(
                    dados_mes["parcela_contrato"]
                ),
                formatar_valor_csv(dados_mes["total_mes"])
            ])

    return nome_arquivo