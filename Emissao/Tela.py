from PySimpleGUI import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome do aluno', size=(10,0)), sg.Input(size=(15,0), key='nome_p')],
            [sg.Text('Responsavel', size=(10,0)), sg.Input(size=(15,0), key='nome_responsavel')],
            [sg.Button('Emitir')]
        ]

        janela = sg.Window("Dados do Usuário").layout(layout)

        self.button, self.values = janela.Read()
    def Iniciar(self):
        nome_pessoa = self.values['nome_pessoa']
        nome_responsavel = self.values['nome_responsavel']


tela = TelaPython()
tela.Iniciar()

