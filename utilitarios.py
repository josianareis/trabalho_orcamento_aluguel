def formatar_moeda(valor):
    valor_formatado = f"{valor:,.2f}"

    valor_formatado = valor_formatado.replace(",", "#")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("#", ".")

    return f"R$ {valor_formatado}"