import PySimpleGUI as sg
import sqlite3


def confirmar():  #função que valida o login
    usuario = values['usuário']
    senha = values['senha']
    banco = sqlite3.connect('banco_cadastro2.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro WHERE usuario = ? AND senha=?", (values['usuário'], values['senha']))
    senha_bd = cursor.fetchone()
    banco.close()
    if senha_bd:
        sg.popup("Bem Vindo ao Sistema Milerte")

    else:
        sg.popup("Dados Inválidos")

def  cadastrar():   #função que cadastra o usuário
    try:
        usuario = values['usuário']
        senha = values['senha']
        banco = sqlite3.connect('banco_cadastro2.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (usuario text,senha text)")
        cursor.execute("INSERT INTO cadastro VALUES ('" + usuario + "','" + senha + "')")
        sg.popup('Usuário Cadastrado com sucesso')
        janela2.hide()
        janela1.un_hide()
        banco.commit()
        banco.close()

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ", erro)

def janeladelogin():
    sg.theme('Purple')
    layout_login = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuário')],
        [sg.Text('Senha')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Button('Ok'), sg.Button('Criar Login')]
    ]
    return sg.Window('Sistema Milerte', layout=layout_login, finalize=True)  # criando janela principal

def janeladecadastro():
    sg.theme('Purple')
    layout_cadastro = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuário')],
        [sg.Text('Senha')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Button('Criar Cadastro')]
    ]
    return sg.Window('Faça seu Cadastro', layout=layout_cadastro, finalize=True)  # criando janela cadastro

janela1, janela2 = janeladelogin(), None

while True:  # criando eventos
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Criar Login':
        janela2 = janeladecadastro()
        janela1.hide()
    if window == janela2 and event == 'Criar Cadastro':
        cadastrar()

    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Ok':
        confirmar()
