import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from modulos_exemplo.funcao_teste import funcao_simulada
import threading
from ttkbootstrap.dialogs import dialogs


class MinhaInterface:
    def __init__(self):
        self.root = ttk.Window(themename='vapor')
        self.root.title("Exemplos Barra de progresso")
 
        self.status_execucao = False

        """
        TODOS OS PARÂMETROS DO METER

        ttk.Meter(
        master=root,
        arcrange=200,             # arco que o indicador vai cobrir, 200°
        arcoffset=-100,           # começar o arco em -100°, para "deslocar" o início
        amounttotal=100,          # valor máximo
        amountused=45,            # valor atual
        amountformat="{:.1f}%",   # formatar o número atual como percentual
        wedgesize=5,              # tamanho do "ponteiro" (wedge)
        metersize=200,            # tamanho da parte visível (200 x 200 px)
        bootstyle='info',         # esquema de cores: info (azul)
        metertype='semi',         # tipo semi-circular
        meterthickness=12,        # espessura da barra
        showtext=True,            # exibir o texto central e laterais
        interactive=True,         # permite interação com o mouse para alterar o valor
        stripethickness=4,        # faixa listrada (striped) com espessura 4
        textleft="Min",           # texto à esquerda
        textright="Max",          # texto à direita
        textfont=('Helvetica', 14, 'bold'),   # fonte para o valor central
        subtext="Progresso atual",            # texto inferior
        subtextstyle='secondary',             # cor do texto inferior
        subtextfont=('Helvetica', 10),        # fonte do texto inferior
        stepsize=5,                # incremento ao arrastar com o mouse
        padding=10                 # padding extra
        """

        # Exemplos
        self.medidor_progresso_1 = ttk.Meter(
            self.root,
            metersize=105,
            padding=1,
            amountused=0,
            metertype="semi",
            interactive=False,
            bootstyle="info",
            stripethickness=10,
            textfont=('Helvetica', 15, 'bold'),
            textright='%'
        )
        self.medidor_progresso_1.pack()

        self.medidor_progresso_2 = ttk.Meter(
            self.root,
            metersize=150,
            padding=5,
            amountused=0,
            metertype="semi",
            subtext="Porcentagem",
            interactive=False,
            bootstyle="danger",
            stripethickness=3,

        )
        self.medidor_progresso_2.pack()

        self.medidor_progresso_3 = ttk.Meter(
            self.root,
            metersize=150,
            padding=2,
            amountused=0,
            metertype="semi",
            subtext="Progresso Total",
            interactive=False,
            bootstyle="success",
            stripethickness=3,
            textright='%'
        )
        self.medidor_progresso_3.pack()

        self.botao_executar = ttk.Button(self.root, text="Iniciar", style='success', command=lambda: self.thread_funcao_externa())
        self.botao_executar.pack()



    def thread_funcao_externa(self):
        threading.Thread(target=self.chamando_funcao_externa, daemon=True).start()

    def chamando_funcao_externa(self):
        if not self.status_execucao:
            self.mudar_status_execucao(True)
            funcao = funcao_simulada(self.atualizar_progresso_geral)

            # Garantindo que no final da função vai aparecer 100%
            self.atualizar_progresso_geral(100)

            # Mudando o status da execução
            self.mudar_status_execucao(False)
        else:
            print('Você ja está executando... espere acabar a execução atual.')

    def mudar_status_execucao(self, status):
        self.status_execucao = status


    def atualizar_progresso_geral(self, valor):
        """ Atualiza o medidor com o valor (0 a 100) """
        self.medidor_progresso_1.configure(amountused=valor)
        self.medidor_progresso_2.configure(amountused=valor)
        self.medidor_progresso_3.configure(amountused=valor)
        self.root.update_idletasks()

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MinhaInterface()
    app.iniciar()
