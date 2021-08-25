# Simulador de dado

from random import randint
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado?"
        #layout
        self.layout = [
            [sg.Text('Jogar o dado?')], 
            [sg.Button('SIM'), sg.Button('NÃO')]
        ]
        

    def Iniciar(self):
        #criar uma janela
        self.janela = sg.Window(title = 'Simulador de Dado', layout=self.layout, margins=(100,50))
        #ler os valores na tela
        self.eventos, self.values = self.janela.Read()
        #fazer alguma coisa com esses valores
        try:
            if self.eventos.lower() == 'sim' or self.eventos.lower() == 's':
                self.GerarValorDoDado()
            elif self.eventos.lower() == 'não' or self.eventos.lower() == 'n':
                print('Agradecemos a sua participação')
            else:
                print('Por favor, digite sim ou não.')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(randint(self.valor_min, self.valor_max))

simulador = SimuladorDeDado()
simulador.Iniciar()