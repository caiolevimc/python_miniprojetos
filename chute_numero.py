from random import randint
import PySimpleGUI as sg

class ChuteNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_max = 100
        self.valor_min = 1
        self.tentar_novamente = True


    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente:
                if int(self.valor_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                    self.PedirValorAleatorio()
                elif int(self.valor_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto!')
                    self.PedirValorAleatorio()
                else:
                    print('\nPARABÉNS! VOCÊ ACEROTU!\n')
                    self.tentar_novamente = False
        except:
            print('\nDIGITE UM NÚMERO!!\n')
            self.Iniciar()
            
        

    def PedirValorAleatorio(self):
        self.valor_chute = input('Chute um numero: ')
    

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = randint(self.valor_min,self.valor_max)


app = ChuteNumero()
app.Iniciar()