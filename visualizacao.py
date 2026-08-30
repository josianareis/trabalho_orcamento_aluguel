import tkinter as tk
from tkinter import ttk

from utilitarios import formatar_moeda


def abrir_planejamento(janela_principal, orcamento):
    janela = tk.Toplevel(janela_principal)

    janela.title("Planejamento anual do orçamento")
    janela.geometry("800x500")
    janela.minsize(700, 450)
    janela.configure(bg="#c59fe0")

    conteudo = ttk.Frame(
        janela,
        padding=20
    )
    conteudo.pack(
        fill="both",
        expand=True
    )

    ttk.Label(
        conteudo,
        text="Planejamento dos 12 meses",
        font=("Arial", 16, "bold"),
        foreground="black"
    ).pack(
        anchor="w",
        pady=(0, 5)
    )

    ttk.Label(
        conteudo,
        text=(
            f"Cliente: {orcamento.nome_cliente} | "
            f"Imóvel: {orcamento.imovel.tipo}"
        ),
        foreground="black"
    ).pack(
        anchor="w",
        pady=(0, 15)
    )

    frame_tabela = ttk.Frame(conteudo)
    frame_tabela.pack(
        fill="both",
        expand=True
    )

    colunas = (
        "mes",
        "aluguel",
        "contrato",
        "total"
    )

    tabela = ttk.Treeview(
        frame_tabela,
        columns=colunas,
        show="headings",
        height=12
    )

    tabela.heading(
        "mes",
        text="Mês"
    )
    tabela.heading(
        "aluguel",
        text="Aluguel"
    )
    tabela.heading(
        "contrato",
        text="Parcela do contrato"
    )
    tabela.heading(
        "total",
        text="Total do mês"
    )

    tabela.column(
        "mes",
        width=70,
        anchor="center"
    )
    tabela.column(
        "aluguel",
        width=180,
        anchor="center"
    )
    tabela.column(
        "contrato",
        width=200,
        anchor="center"
    )
    tabela.column(
        "total",
        width=180,
        anchor="center"
    )

    barra_rolagem = ttk.Scrollbar(
        frame_tabela,
        orient="vertical",
        command=tabela.yview
    )
    tabela.configure(
        yscrollcommand=barra_rolagem.set
    )

    tabela.pack(
        side="left",
        fill="both",
        expand=True
    )
    barra_rolagem.pack(
        side="right",
        fill="y"
    )

    planejamento = orcamento.gerar_planejamento_anual()

    for dados_mes in planejamento:
        tabela.insert(
            "",
            "end",
            values=(
                dados_mes["mes"],
                formatar_moeda(dados_mes["aluguel"]),
                formatar_moeda(
                    dados_mes["parcela_contrato"]
                ),
                formatar_moeda(dados_mes["total_mes"])
            )
        )

    janela.transient(janela_principal)
    janela.focus()