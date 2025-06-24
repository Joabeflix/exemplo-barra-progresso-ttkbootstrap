import time
import random

def funcao_simulada(funcao_atualizar_barra):

    qtd_total_simulada = 100
    qtd_feita = 0

    for x in range(qtd_total_simulada):

        # Emulando um tempo para simular como se fosse alguma função do seu programa que demora tempo relativo e etc
        time.sleep((random.random() * 1.2))

        if funcao_atualizar_barra:
            progresso = int((qtd_feita / qtd_total_simulada) * 100)
            funcao_atualizar_barra(progresso)

        qtd_feita+=1




