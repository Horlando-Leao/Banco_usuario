import pathlib
import idlelib.PathBrowser
caminho = pathlib.Path(r'C:/home/horlando/Área de Trabalho/Banco_usuario/src/backend/dml.py')

from dml import inserir_usuario_no_banco
from dml import excluir_usuario_no_banco
from dml import atualizar_usuario_no_banco
from dml import pesquisar_usuario_no_banco
import sys
import os
import platform


def opcao_criar_usuario():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('E-mail: ')

    inserir_usuario_no_banco(nome, telefone, email)
    os.system('cls') if platform.system()=="Windows" else os.system('clear')
    opcao_menu_principal()

def opcao_pesquisar_usuario():
    print('1:NOME\n2:TELEFONE\n3:EMAIL')
    x = input('Campo a pesquisar: ')
    if x == '1':
        campo = "nome"
    elif x == '2':
        campo = "telefone"
    elif x == '3':
        campo = "email"
    else:
        campo = "nome"

    print('CAMPO A PESQUISAR POR%s' %campo)
    valor_pesquisa = str(input(r"Valor respectivo ao campo escolhido: "))
    aspas1 = '"'
    aspas2 = '"'
    valor_pesquisa = ('{}{}{}').format(aspas1, valor_pesquisa, aspas2)
    pesquisar_usuario_no_banco(valor_pesquisa, campo)
    opcao_menu_principal()

def opcao_atualizar_usuario():
    nome = input('Nome: ')
    email = input('E-mail: ')

    atualizar_usuario_no_banco(nome, email)
    os.system('cls') if platform.system()=="Windows" else os.system('clear')
    opcao_menu_principal()

def opcao_excluir_usuario():
    email = input('E-mail: ')

    excluir_usuario_no_banco(email)
    os.system('cls') if platform.system()=="Windows" else os.system('clear')
    opcao_menu_principal()

def opcao_menu_principal():
    print('MENU')
    print("1:CRIAR NOVO USUARIO\n2:CONSULTAR USUÁRIO\n3:ATUALIZAR USUÁRIO\n4:EXCLUIR USUÁRIO")
    print('0:SAIR')
    
    escolha = int(input('OPÇÃO: '))
    if escolha == 1:
     opcao_criar_usuario()
    elif escolha == 2:
        opcao_pesquisar_usuario()
    elif escolha == 3:
        opcao_atualizar_usuario()
    elif escolha == 4:
        opcao_excluir_usuario()
    elif escolha == 0:
        print('Até mais!')
    else:
        print('digite uma opção válida!')
        opcao_menu_principal()

opcao_menu_principal()
