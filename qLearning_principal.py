# -*- coding: utf-8 -*-
import numpy as np
from my_qLearning_procura_chave import procura_chave
from maze_env import Maze

class QLearning_Table:

    def __init__(self):

        self.gamma = 0.50
        self.taxa_random = 0.90
        self.dict_Q = {'chave1': [[1, 3], [0, 0]], 'chave2': [[1, 3, 4], [0, 0, 0]], 'chave3': [[1, 3, 4], [0, 0, 0]],
                       'chave4': [[1, 3, 4], [0, 0, 0]], 'chave5': [[1, 3, 4], [0, 0, 0]],
                       'chave6': [[1, 3, 4], [0, 0, 0]], 'chave7': [[1, 3, 4], [0, 0, 0]],
                       'chave8': [[1, 3, 4], [0, 0, 0]], 'chave9': [[1, 3, 4], [0, 0, 0]],
                       'chave10': [['terminal'], [0]],
                       'chave11': [[1, 2, 3], [0, 0, 0]], 'chave12': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave13': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave14': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave15': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave16': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave17': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave18': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave19': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave20': [[1, 2, 4], [0, 0, 0]],
                       'chave21': [[1, 2, 3], [0, 0, 0]], 'chave22': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave23': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave24': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave25': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave26': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave27': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave28': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave29': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave30': [[1, 2, 4], [0, 0, 0]],
                       'chave31': [[1, 2, 3], [0, 0, 0]], 'chave32': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave33': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave34': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave35': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave36': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave37': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave38': [[1, 2, 3, 4], [0, 0, 0, 0]], 'chave39': [[1, 2, 3, 4], [0, 0, 0, 0]],
                       'chave40': [[1, 2, 4], [0, 0, 0]],
                       'chave41': [[2, 3], [0, 0]], 'chave42': [[2, 3, 4], [0, 0, 0]],
                       'chave43': [[2, 3, 4], [0, 0, 0]], 'chave44': [[2, 3, 4], [0, 0, 0]],
                       'chave45': [[2, 3, 4], [0, 0, 0]],
                       'chave46': [[2, 3, 4], [0, 0, 0]], 'chave47': [[2, 3, 4], [0, 0, 0]],
                       'chave48': [[2, 3, 4], [0, 0, 0]], 'chave49': [[2, 3, 4], [0, 0, 0]], 'chave50': [[2, 4], [0, 0]]
                       }


    def movimenta_explorador(self, action, linha, coluna):

        if action == 1:
            linha = linha + 1
        elif action == 2:
            linha = linha - 1
        elif action == 3:
            coluna = coluna + 1
        elif action == 4:
            coluna = coluna - 1

        return linha, coluna

    def escolhe_acao(self, explorador):
        resposta_chave = procura_chave(explorador, self.dict_Q)
        lista_actions = resposta_chave[0]
        lista_rewards = resposta_chave[1]
        if np.random.uniform() < self.taxa_random:
            # escolhe o maior valor da lista de rewards
            reward = max(lista_rewards)
            indice_maior_reward = lista_rewards.index(reward)
            best_action = lista_actions[indice_maior_reward]
        else:
            best_action = np.random.choice(lista_actions)
            indice_best_action = lista_actions.index(best_action)
            reward = lista_rewards[indice_best_action]

        return best_action

    def atualiza_tabela_Q(self, explorador, action,  reward):
        exploradorX = str(explorador)
        chave = 'chave' + exploradorX

        retorno_dict = procura_chave(explorador, self.dict_Q)
        lista_actions = retorno_dict[0]
        indice = lista_actions.index(action)
        self.dict_Q[chave][1][indice] = reward

        return

    def learn(self, explorador, explorador2):

        if explorador2 == 10:
            reward = 100
            terminou = True
            motivo = 'Chegou no objetivo'
        elif explorador2 in [2, 3, 4, 5, 6, 7, 8, 9, 14, 18, 32, 33, 35, 36, 38, 45, 46]:
            reward = -100
            terminou = False
            motivo = 'Bateu no bloco preto'
        else:
            reward = -1
            terminou = False
            motivo = 'Continua'

        verificador = procura_chave(explorador2, self.dict_Q)

        if verificador[0] != 'terminal':
            verificador2 = verificador[1]

        if verificador[0] != 'terminal':
            q_reward = reward + self.gamma * max(verificador2)
        else:
            q_reward = reward

        return q_reward, terminou, motivo

    def verifica_copia(self, copia_Q):


        teste = self.dict_Q.values()
        if copia_Q == teste:
            return 'parou'
        else:

            return 'continua'



def update():
    tabela_Q = QLearning_Table()
    matriz_de_transicao = np.arange(1, 51).reshape(5, 10)
    primeira_vez = True
    copia_tabela_Q = []
    for episodio in range (1,1001):
        linha = 0
        coluna = 0
        env.reset()
        recompensa_ep = 0
        conta_passos = 0
        terminou = False
        lista_passos = []
        lista_reward = []

        while terminou != True:
            env.render()
            explorador = matriz_de_transicao[linha][coluna]
            #ESCOLHE A AÇÃO
            action = tabela_Q.escolhe_acao(explorador)
            env.step(action)
            #MOVIMENTA O EXPLORADOR
            linha, coluna = tabela_Q.movimenta_explorador(action = action, linha = linha, coluna = coluna)
            explorador2 = matriz_de_transicao[linha][coluna]
            #APRENDIZADO
            final_reward, terminou, motivo = tabela_Q.learn(action, explorador2)
            tabela_Q.atualiza_tabela_Q(explorador, action, final_reward)
            conta_passos = conta_passos + 1
            lista_passos.append(explorador)
            lista_reward.append(final_reward)
            recompensa_ep = recompensa_ep + final_reward

        if motivo == 'Chegou no objetivo':
            if primeira_vez == True:
                politica_otima = lista_passos
                politica_otima_reward = lista_reward
                primeira_vez = False
                controle_passos = []
            else:
                if (len(politica_otima)>len(lista_passos)):
                    politica_otima = lista_passos
                    politica_otima_reward = lista_reward
                    passos_politica_otima = conta_passos
                    if politica_otima == controle_passos:
                        cont = cont + 1
                        print(cont)
                        if cont == 3:
                            print('entrou')
                            break
                    else:
                        controle_passos = politica_otima

        #TESTA SE NAO HOUVE MUDANÇA NA TABELA Q SE PERMANECE IGUAL FINALIZA O APRENDIZADO
        if episodio % 50 == 0:
            x  = tabela_Q.verifica_copia(copia_Q = copia_tabela_Q)
            if x == 'parou':
                break
            else:
                copia_tabela_Q = tabela_Q.dict_Q.values()


        print('Fim do episodio: {} \nNumero de passos: {}'.format(episodio, conta_passos))
        print('Recompensa do episódio: {}'.format(recompensa_ep))
        print('Motivo: {}'.format(motivo))
        print('Movimentos: {}'.format(lista_passos))
        print('------------------------------------------------------------')
    print('----------------------------------------')
    print('Politica Otima:')
    print(politica_otima)
    print('Recompensas para política ótima')
    print(politica_otima_reward)
    print('Numero de Passos da política ótima')
    print(passos_politica_otima)


if __name__ == "__main__":

    env = Maze()
    env.after(100, update)
    env.mainloop()

