from tkinter import *
from dml import *
"""aqui é aonde vai acontecer a conversão de dados que recebera do front-end para o dml.py e , assim também como vou receber dados da web ou do banco e converter para aparecer bonitinho no 
front-end"""

def Converter_enviar_para_dml_inserir_usuario(nome, telefone, email):
    try:
        inserir_usuario_no_banco(nome, telefone, email)
    except Exception as e:
        rotulo5 = Label(janela_1, text=sys.exc_info())
        rotulo5.place(x = 176, y = 350)
        rotuloZ = Label(janela_1, text=e)
        rotuloZ.place(x = 176, y = 380)
   
def Converter_enviar_para_dml_pesquisar_usuario(valor_pesquisa, campo):
    try:
        aspas1 = "'"
        aspas2 = "'"
        valor_pesquisa = ('{}{}{}').format(aspas1, valor_pesquisa, aspas2)
        pesquisar_usuario_no_banco(valor_pesquisa, campo)
    except Exception as e:
        rotulo5 = Label(janela_1, text=sys.exc_info())
        rotulo5.place(x = 176, y = 350)
        rotuloZ = Label(janela_1, text=e)
        rotuloZ.place(x = 176, y = 380)

def Converter_enviar_para_atualizar_usuario(nome, email):
    try:
        atualizar_usuario_no_banco(nome, email)
    except Exception as e:
        rotulo5 = Label(janela_1, text=sys.exc_info())
        rotulo5.place(x = 176, y = 350)
        rotuloZ = Label(janela_1, text=e)
        rotuloZ.place(x = 176, y = 380)
    
def Converter_enviar_para_dml_excluir_usuario(email):
    try:
        atualizar_usuario_no_banco(email)
    except Exception as e:
        rotulo5 = Label(janela_1, text=sys.exc_info())
        rotulo5.place(x = 176, y = 350)
        rotuloZ = Label(janela_1, text=e)
        rotuloZ.place(x = 176, y = 380)
