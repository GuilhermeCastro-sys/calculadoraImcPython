'''
Calculadora de IMC
'''

# Este projeto não substitui ou limita as possibilidades medicinais, procure um médico se for preciso

# Bibliotecas importadas para o projeto
import PySimpleGUI as sg

# Definições para as estruturas condicionais do IMC
def retornarValores(imc):

    if (imc < 18.5):
        return 'Abaixo do peso'
    elif (imc >= 18.5 and imc <= 24.9):
        return 'Peso Normal'
    elif (imc >= 25 and imc <= 29.9):
        return 'Sobrepeso'
    elif (imc >= 30.0 and imc <= 34.9):
        return 'Obesidade Grau I'
    elif (imc >= 35.0 and imc <= 39.9):
        return 'Obesidade Grau II'
    elif (imc >= 40):
        return 'Obesidade Grau III'

# temas do projeto (opcional)
sg.theme('Reddit')

# Definição do Layout
layout = [[sg.Text('Calculadora de IMC', font=('Eras Bold ITC', 16))],
            [sg.Frame(layout=[[sg.Text('Informe seu peso (kg)', font=('Corbel', 12))],
                            [sg.Input(size=(20,1), key='peso')],
                            [sg.Text('Informe sua altura (metro)', font=('Corbel', 12))],
                            [sg.Input(size=(20,1), key='altura')],
                            [sg.Text('PREENCHA OS CAMPOS ACIMA!', text_color=('red'), visible=False, key='aviso')]], 
                            title = 'Indice de Massa Corporal', font=('Corbel', 14))],
                            [sg.Button('Calcular', size=(25,1))],
                            [sg.Text('IMC: '), sg.Input(size=(10,1), disabled=True, key='imc', justification='center')],
                            [sg.Text('Resultado: ', size=(25,1), key='resultado')],
                            [sg.Output(size=(27,10), key='informacoes')],
                            [sg.Button('Limpar', size=(25,1))]]

# Definição da janela de minimizar e finalizar
window = sg.Window('Seu peso, Sua saúde', layout=layout, finalize=True)

# Definição dos loops de eventos para o projeto continuar rodando
while True:
    events, values = window.Read()
    if events == sg.WINDOW_CLOSED:
        break
    # Estruturas condicionais dos eventos
    if events == 'Calcular' and values['peso'] == '' or values['altura'] == '':
    # Caso as entradas de dados de peso ou de altura estiverem em branco, um aviso surgirá
        window.Element('aviso').Update(visible=True)
    if events == 'Calcular' and values['peso'] != '' and values['altura'] != '':
        window.Element('aviso').Update(visible=False)
        peso = float(values['peso'].replace(',','.'))
        altura = float(values['altura'].replace(',','.'))
        calculo = peso / (altura * altura)
        calculo = round(calculo, 1)
        window.Element('resultado').Update(value='Resultado: {0}\n'.format(retornarValores(calculo)), visible=True)
        window.Element('imc').Update(disabled=False, value=calculo)

        # evento que o Output apresentará através da def das linhas 9 a 22
        if (calculo < 18.5):
            window.Element('informacoes').Update(value='Recomendações:\n\nEstimule a fome, se alimentan-\ndo a cada 3 horas, tentando \nfazer de 5 a 6 refeições por dia.' 
            '\n\nCafé da manhã, lanche, almoço, lanche, jantar e um lanche antes de dormir. O maior fracionamento permite você \ncontrolar melhor seu apetite.')
        elif (calculo >= 18.5 and calculo <= 24.9):
            window.Element('informacoes').Update(value='Recomendações:\n\nContinue consumindo alimentos \ncomo fontes de proteína magra e de carboidratos integrais\n\nOPCIONAIS')
        elif (calculo >= 25.0 and calculo <= 29.9):
            window.Element('informacoes').Update(value='Recomendações:\n\nManter uma atividade física re-\ngular como caminhadas, boa \nalimentação e acompanhamento médico\n\nOPCIONAL')
        elif (calculo >= 30.0 and calculo <= 34.9):
            window.Element('informacoes').Update(value='Recomendações:\n\nProcurar um médico para avaliar a situação\n\nOPCIONAL, porém RECOMEN-\nDADO')
        elif (calculo >= 35.0 and calculo <= 39.9):
            window.Element('informacoes').Update(value='Recomendações:\n\nProcurar um médico para avaliar a situação\n\nOPCIONAL, porém RECOMEN-\nDADO')
        else:
            window.Element('informacoes').Update(value='Recomendações:\n\nProcurar um médico para avaliar a situação\n\nOPCIONAL, porém RECOMEN-\nDADO')

    # Evento do comando Limpar
    if events == 'Limpar':
        window.Element('peso').Update(value = '')
        window.Element('altura').Update(value = '')
        window.Element('imc').Update(value='', disabled=True)
        window.Element('resultado').Update(value = 'Resultado: ')
        window.Element('informacoes').Update(value = '')

window.close()