import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from imoveis import Apartamento, Casa, Estudio
from orcamento import Orcamento
from utilitarios import formatar_moeda
from visualizacao import abrir_planejamento
from gerador_csv import gerar_csv


class AplicacaoOrcamento:
    def __init__(self, janela):
        self.janela = janela

        self.janela.title(
            "R.M Imobiliária - Orçamento de Aluguel"
        )
        self.janela.geometry("1000x700")
        self.janela.minsize(900, 650)
        self.janela.configure(bg="#c59fe0")

        self.nome_cliente = tk.StringVar()
        self.tipo_imovel = tk.StringVar(
            value="Apartamento"
        )
        self.quantidade_parcelas = tk.IntVar(
            value=5
        )

        self.quartos = tk.IntVar(value=1)
        self.tem_garagem = tk.BooleanVar(value=False)
        self.possui_criancas = tk.BooleanVar(value=True)
        self.quantidade_vagas = tk.IntVar(value=0)

        self.orcamento_atual = None

        self.texto_resultado = tk.StringVar(
        value="Preencha os dados e calcule o orçamento."
    )

        self.configurar_estilos()
        self.criar_interface()

    def configurar_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "TFrame",
            background="#c59fe0"
        )

        estilo.configure(
            "TLabel",
            font=("Arial", 11),
            background="#c59fe0"
        )

        estilo.configure(
            "Titulo.TLabel",
            font=("Arial", 22, "bold"),
            foreground="black",
            background="#79e2a1"
        )

        estilo.configure(
            "Subtitulo.TLabel",
            font=("Arial", 15, "bold"),
            foreground="black",
            background="#c59fe0"
        )

        estilo.configure(
            "TLabelframe",
            background="#c59fe0"
        )

        estilo.configure(
            "TLabelframe.Label",
            font=("Arial", 11, "bold"),
            foreground="black",
            background="#c59fe0"
        )

        estilo.configure(
            "TCheckbutton",
            font=("Arial", 10),
            background="#c59fe0"
        )

    def criar_interface(self):
        cabecalho = tk.Frame(
            self.janela,
            bg="#79e2a1",
            height=90
        )
        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)

        titulo = ttk.Label(
            cabecalho,
            text="R.M Imobiliária",
            style="Titulo.TLabel"
        )
        titulo.pack(pady=(18, 0))

        descricao = tk.Label(
            cabecalho,
            text="Sistema de Orçamento de Aluguel",
            font=("Arial", 11),
            foreground="black",
            background="#79e2a1"
        )
        descricao.pack()

        conteudo = ttk.Frame(
            self.janela,
            padding=25
        )
        conteudo.pack(
            fill="both",
            expand=True
        )

        subtitulo = ttk.Label(
            conteudo,
            text="Dados do orçamento",
            style="Subtitulo.TLabel"
        )
        subtitulo.pack(anchor="w")

        separador = ttk.Separator(
            conteudo,
            orient="horizontal"
        )
        separador.pack(
            fill="x",
            pady=(8, 20)
        )

        formulario = ttk.Frame(conteudo)
        formulario.pack(
            fill="x",
            pady=(0, 15)
        )
        formulario.columnconfigure(
            1,
            weight=1
        )

        ttk.Label(
            formulario,
            text="Nome do cliente:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=7
        )

        self.campo_nome = ttk.Entry(
            formulario,
            textvariable=self.nome_cliente,
            width=45
        )
        self.campo_nome.grid(
            row=0,
            column=1,
            sticky="ew",
            pady=7
        )

        ttk.Label(
            formulario,
            text="Tipo de imóvel:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=7
        )

        self.campo_tipo = ttk.Combobox(
            formulario,
            textvariable=self.tipo_imovel,
            values=[
                "Apartamento",
                "Casa",
                "Estúdio"
            ],
            state="readonly",
            width=25
        )
        self.campo_tipo.grid(
            row=1,
            column=1,
            sticky="w",
            pady=7
        )

        self.campo_tipo.bind(
            "<<ComboboxSelected>>",
            self.atualizar_opcoes_imovel
        )

        ttk.Label(
            formulario,
            text="Parcelas do contrato:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=7
        )

        self.campo_parcelas = ttk.Combobox(
            formulario,
            textvariable=self.quantidade_parcelas,
            values=[1, 2, 3, 4, 5],
            state="readonly",
            width=10
        )
        self.campo_parcelas.grid(
            row=2,
            column=1,
            sticky="w",
            pady=7
        )

        self.frame_opcoes = ttk.LabelFrame(
            conteudo,
            text="Opções do imóvel",
            padding=15
        )
        self.frame_opcoes.pack(
            fill="x",
            pady=(10, 15)
        )


        frame_botoes = ttk.Frame(conteudo)
        frame_botoes.pack(
            fill="x",
            pady=(0, 15)
        )

        self.botao_calcular = ttk.Button(
            frame_botoes,
            text="Calcular orçamento",
            command=self.calcular_orcamento
        )
        self.botao_calcular.pack(
            side="left",
            padx=(0, 10)
        )

        self.botao_planejamento = ttk.Button(
            frame_botoes,
            text="Ver planejamento de 12 meses",
            command=self.mostrar_planejamento,
            state="disabled"
        )
        self.botao_planejamento.pack(
            side="left"
        )
        self.botao_csv = ttk.Button(
            frame_botoes,
            text="Gerar arquivo CSV",
            command=self.salvar_csv,
            state="disabled"
        )
        self.botao_csv.pack(
            side="left",
            padx=(10, 0)
        ) 
        self.label_resultado = tk.Label(
    conteudo,
    textvariable=self.texto_resultado,
    font=("Arial", 11),
    foreground="black",
    background="white",
    justify="left",
    anchor="w",
    padx=15,
    pady=12,
    relief="solid",
    borderwidth=1
)
        self.label_resultado.pack(
    fill="x",
    pady=(0, 15)
)

        self.atualizar_opcoes_imovel()

        self.campo_nome.focus()

    def limpar_opcoes_imovel(self):
        componentes = self.frame_opcoes.winfo_children()

        for componente in componentes:
            componente.destroy()

    def atualizar_opcoes_imovel(self, evento=None):
        self.limpar_opcoes_imovel()

        tipo = self.tipo_imovel.get()

        if tipo == "Apartamento" or tipo == "Casa":
            ttk.Label(
                self.frame_opcoes,
                text="Quantidade de quartos:"
            ).grid(
                row=0,
                column=0,
                sticky="w",
                padx=(0, 10),
                pady=7
            )

            campo_quartos = ttk.Combobox(
                self.frame_opcoes,
                textvariable=self.quartos,
                values=[1, 2],
                state="readonly",
                width=10
            )
            campo_quartos.grid(
                row=0,
                column=1,
                sticky="w",
                pady=7
            )

            ttk.Checkbutton(
                self.frame_opcoes,
                text="Adicionar garagem (+ R$ 300,00)",
                variable=self.tem_garagem
            ).grid(
                row=1,
                column=0,
                columnspan=2,
                sticky="w",
                pady=7
            )

            if tipo == "Apartamento":
                ttk.Checkbutton(
                    self.frame_opcoes,
                    text="O cliente possui crianças",
                    variable=self.possui_criancas
                ).grid(
                    row=2,
                    column=0,
                    columnspan=2,
                    sticky="w",
                    pady=7
                )

                ttk.Label(
                    self.frame_opcoes,
                    text=(
                        "Desmarque a opção acima para "
                        "aplicar o desconto de 5%."
                    )
                ).grid(
                    row=3,
                    column=0,
                    columnspan=2,
                    sticky="w",
                    pady=(0, 7)
                )

        elif tipo == "Estúdio":
            ttk.Label(
                self.frame_opcoes,
                text="Quantidade de vagas:"
            ).grid(
                row=0,
                column=0,
                sticky="w",
                padx=(0, 10),
                pady=7
            )

            campo_vagas = ttk.Spinbox(
                self.frame_opcoes,
                textvariable=self.quantidade_vagas,
                from_=0,
                to=20,
                increment=1,
                width=10
            )
            campo_vagas.grid(
                row=0,
                column=1,
                sticky="w",
                pady=7
            )

            ttk.Label(
                self.frame_opcoes,
                text=(
                    "Informe zero vaga ou, no mínimo, "
                    "duas vagas."
                )
            ).grid(
                row=1,
                column=0,
                columnspan=2,
                sticky="w",
                pady=7
            )

    def criar_imovel(self):
        tipo = self.tipo_imovel.get()

        if tipo == "Apartamento":
            return Apartamento(
                quartos=self.quartos.get(),
                tem_garagem=self.tem_garagem.get(),
                possui_criancas=self.possui_criancas.get()
            )

        if tipo == "Casa":
            return Casa(
                quartos=self.quartos.get(),
                tem_garagem=self.tem_garagem.get()
            )

        if tipo == "Estúdio":
            return Estudio(
                quantidade_vagas=self.quantidade_vagas.get()
            )

        raise ValueError("Selecione um tipo de imóvel.")

    def calcular_orcamento(self):
        try:
            imovel = self.criar_imovel()

            self.orcamento_atual = Orcamento(
                nome_cliente=self.nome_cliente.get(),
                imovel=imovel,
                quantidade_parcelas=(
                    self.quantidade_parcelas.get()
                )
            )

            valor_aluguel = imovel.calcular_aluguel()

            valor_parcela = (
                self.orcamento_atual
                .calcular_parcela_contrato()
            )

            planejamento = (
                self.orcamento_atual
                .gerar_planejamento_anual()
            )

            total_com_contrato = (
                planejamento[0]["total_mes"]
            )

            resultado = (
                f"Cliente: {self.orcamento_atual.nome_cliente}\n"
                f"Imóvel: {imovel.tipo}\n"
                f"Aluguel mensal: "
                f"{formatar_moeda(valor_aluguel)}\n"

                f"Contrato: "
                f"{formatar_moeda(Orcamento.VALOR_CONTRATO)} "
                f"em {self.orcamento_atual.quantidade_parcelas} "
                f"vez(es)\n"

                f"Parcela do contrato: "
                f"{formatar_moeda(valor_parcela)}\n"

                f"Total mensal durante o parcelamento: "
                f"{formatar_moeda(total_com_contrato)}"
            )

            self.texto_resultado.set(resultado)
            self.botao_planejamento.config(
                state="normal"
            )

            self.botao_csv.config(
                state="normal"
            )

        except ValueError as erro:
            self.orcamento_atual = None

            self.botao_planejamento.config(
                state="disabled"
            )

            self.botao_csv.config(
                state="disabled"
            )

            messagebox.showerror(
                "Dados inválidos",
                str(erro),
                parent=self.janela
            )

        except tk.TclError:
            self.orcamento_atual = None

            self.botao_planejamento.config(
                state="disabled"
            )

            self.botao_csv.config(
                state="disabled"
            )

            messagebox.showerror(
                "Dados inválidos",
                "Preencha os campos com valores válidos.",
                parent=self.janela
            )

    def iniciar(self):
        self.janela.mainloop()

    def mostrar_planejamento(self):
        if self.orcamento_atual is None:
            self.botao_planejamento.config(
                state="disabled"
            )
            self.botao_csv.config(
                state="disabled"
            )
            messagebox.showwarning(
                "Orçamento não calculado",
                "Calcule um orçamento antes de continuar.",
                parent=self.janela
            )
            return

        abrir_planejamento(
            self.janela,
            self.orcamento_atual
        )

    def salvar_csv(self):
        if self.orcamento_atual is None:
            self.botao_planejamento.config(
                state="disabled"
            )
            self.botao_csv.config(
                state="disabled"
            )
            messagebox.showwarning(
                "Orçamento não calculado",
                "Calcule um orçamento antes de gerar o CSV.",
                parent=self.janela
            )
            return
        
        nome_cliente = (
            self.orcamento_atual
            .nome_cliente
            .strip()
            .replace(" ", "_")
        )

        nome_sugerido = (
            f"orcamento_{nome_cliente}.csv"
        )

        caminho_arquivo = filedialog.asksaveasfilename(
            parent=self.janela,
            title="Salvar orçamento",
            initialfile=nome_sugerido,
            defaultextension=".csv",
            filetypes=[
                ("Arquivo CSV", "*.csv")
            ]
        )

        if not caminho_arquivo:
            return

        try:
            gerar_csv(
                self.orcamento_atual,
                caminho_arquivo
            )

            messagebox.showinfo(
                "Arquivo gerado",
                (
                    "O arquivo CSV foi gerado "
                    "com sucesso."
                ),
                parent=self.janela
            )

        except OSError as erro:
            messagebox.showerror(
                "Erro ao gerar arquivo",
                str(erro),
                parent=self.janela
            )


def iniciar_aplicacao():
    janela = tk.Tk()

    aplicacao = AplicacaoOrcamento(janela)

    aplicacao.iniciar()